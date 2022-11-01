from typing import Any

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from main.models import Question, Test, UserResult, Answer

User = get_user_model()


class QuestionsListView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_REDIRECT_URL
    model = Question

    def get(self, request: WSGIRequest, *args, **kwargs):
        return self.__render()

    def post(self, request: WSGIRequest, *args, **kwargs):
        self.__register_answer()
        return self.__render()

    def __render(self) -> HttpResponse:
        if self.__is_complete_test():
            return render(request=self.request,
                          template_name='main/completed_test.html',
                          context=self.__generate_completed_context())
        return render(request=self.request,
                      template_name='main/uncompleted_test.html',
                      context=self.__generate_uncompleted_context())

    def __is_complete_test(self) -> bool:
        return len(self.__provide_uncompleted_questions()) == 0

    def __provide_uncompleted_questions(self) -> QuerySet[Question]:
        completed_question_ids = self.__user_results().values_list('question', flat=True)
        return Question.objects.filter(test=self.__get_test()).exclude(id__in=completed_question_ids)

    def __user_results(self) -> QuerySet[UserResult]:
        return UserResult.objects.filter(user=self.request.user).filter(question__test=self.__get_test())

    def __get_test(self) -> Test:
        test_id = self.kwargs['test_id']
        return Test.objects.get(pk=test_id)

    def __generate_completed_context(self) -> dict[str, Any]:
        return {
            'test': self.__get_test(),
            'user_answers': self.__user_answers()
        }

    def __user_answers(self) -> QuerySet[Answer]:
        answer_ids = self.__user_results().values_list('answer', flat=True)
        return Answer.objects.filter(id__in=answer_ids)

    def __generate_uncompleted_context(self) -> dict[str, Any]:
        new_question = self.__provide_uncompleted_questions().first()
        return {
            'test': self.__get_test(),
            'question': new_question,
            'answers': new_question.answer_set.order_by('?')  # Случайно перемешиваем
        }

    def __register_answer(self) -> None:
        question_id = int(self.request.POST.get('question_id'))
        selected_answer_ids = [int(id_) for id_ in self.request.POST.getlist('answer_id')]
        for selected_answer_id in selected_answer_ids:
            answer_ = Answer.objects.get(pk=selected_answer_id)
            question_ = Question.objects.get(pk=question_id)
            UserResult.objects.update_or_create(user=self.request.user, question=question_, answer=answer_)
