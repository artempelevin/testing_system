from django.contrib import admin
from django.contrib.admin import display
from nested_admin.nested import NestedModelAdmin

from main.models import UserResult


@admin.register(UserResult)
class UserResultAdmin(NestedModelAdmin):
    list_filter = ('user', 'question__test')
    list_display = ('user', 'question', 'answer', 'get_is_right')
    list_display_links = ('user', 'question')
    readonly_fields = ('user', 'question', 'answer')

    @display(ordering='answer__is_right', description='Правильность')
    def get_is_right(self, obj: UserResult):
        return '✔' if obj.answer.is_right else '❌'

    def has_add_permission(self, request):  # Скрыли кнопку "Добавить" (ибо нефиг:D)
        return "add" in request.path or "change" in request.path
