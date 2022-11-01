from django.contrib import admin
from django.contrib.admin import display
from nested_admin.nested import NestedModelAdmin

from main.models import UserResult


@admin.register(UserResult)
class UserResultAdmin(NestedModelAdmin):
    list_filter = ('user', 'question__test__test_suite', 'question__test', 'answer__is_right')
    list_display = ('user', 'get_test_suite', 'get_test', 'question', 'answer', 'get_is_right')
    list_display_links = ('user', 'question')
    readonly_fields = ('user', 'question', 'answer')

    @display(ordering='question__test__test_suite', description='Набор тестов')
    def get_test_suite(self, obj: UserResult):
        return obj.question.test.test_suite

    @display(ordering='question__test', description='Тест')
    def get_test(self, obj: UserResult):
        return obj.question.test

    @display(ordering='answer__is_right', description='Правильность')
    def get_is_right(self, obj: UserResult):
        return '✔' if obj.answer.is_right else '❌'

    def has_add_permission(self, request):  # Скрыли кнопку "Добавить" (ибо нефиг:D)
        return "add" in request.path or "change" in request.path
