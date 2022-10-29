from django import forms
from django.core.exceptions import ValidationError
from django.http import QueryDict


class QuestionForm(forms.ModelForm):
    def clean(self):
        super(QuestionForm, self).clean()
        # Ток так можно получить все данные формы, поэтому далее идут некоторые костыли по проверке ответов:)
        form_data_ = self.data
        num_of_answers_ = int(form_data_.get('answer_set-TOTAL_FORMS', 0))
        num_of_right_answers = self.__provide_num_of_right_answers(form_data=form_data_, num_of_answers=num_of_answers_)

        if num_of_answers_ < 2:
            raise ValidationError('У вопроса должен быть минимум 2 ответа')
        if num_of_right_answers == 0:
            raise ValidationError('Должен быть хотя бы 1 правильный ответ')
        if num_of_answers_ == num_of_right_answers:
            raise ValidationError('Все ответы не могут быть правильными')

    @staticmethod
    def __provide_num_of_right_answers(form_data: QueryDict, num_of_answers: int) -> int:
        return sum(1 for i in range(num_of_answers)
                   if form_data.get(f"answer_set-{i}-is_right", 'off') == 'on')
