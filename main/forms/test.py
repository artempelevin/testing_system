from django import forms
from django.core.exceptions import ValidationError
from django.http import QueryDict


class TestForm(forms.ModelForm):

    def clean(self):
        super(TestForm, self).clean()

        title = self.cleaned_data.get('title')
        if len(title) > 255:
            self.add_error('title', 'Тема теста должна убираться 255 символов')

        form_data_ = self.data
        self.__validate_questions(form_data=form_data_)

    def __validate_questions(self, form_data: QueryDict) -> None:
        # Ток так можно получить все данные формы, поэтому далее идут некоторые костыли по проверке ответов:)
        num_of_questions = int(form_data.get('question_set-TOTAL_FORMS', 0))
        if num_of_questions < 1:
            raise ValidationError('У теста должен быть хотя бы 1 вопрос')

        for question_index_ in range(num_of_questions):
            question_text_ = form_data.get(f"question_set-{question_index_}-text")
            if not question_text_:
                raise ValidationError('У всех вопросов должен быть заполнен текст вопроса')
            self.__validate_answers(form_data=form_data, question_index=question_index_,
                                    question_text=question_text_)

    def __validate_answers(self, form_data: QueryDict, question_index: int, question_text: str) -> None:

        num_of_answers_ = int(form_data.get(f"question_set-{question_index}-answer_set-TOTAL_FORMS", 0))
        num_of_right_answers = self.__provide_num_of_right_answers(form_data=form_data,
                                                                   question_index=question_index,
                                                                   num_of_answers=num_of_answers_)
        if num_of_answers_ < 2:
            raise ValidationError(f"У вопроса '{question_text}' должен быть минимум 2 ответа")
        if num_of_right_answers == 0:
            raise ValidationError(f"У вопроса '{question_text}' должен быть хотя бы 1 правильный ответ")
        if num_of_answers_ == num_of_right_answers:
            raise ValidationError(f"У вопроса '{question_text}' все ответы не могут быть правильными")

    @staticmethod
    def __provide_num_of_right_answers(form_data: QueryDict, question_index: int, num_of_answers: int) -> int:
        return sum(1 for i in range(num_of_answers)
                   if form_data.get(f"question_set-{question_index}-answer_set-{i}-is_right", 'off') == 'on')
