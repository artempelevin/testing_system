from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import Textarea
from nested_admin.nested import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from main.models import Test, Question, Answer


class _AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return

        answers: list[Answer] = [form.instance for form in self.forms]
        right_answers = [answer for answer in answers if answer.is_right]
        if len(answers) < 2:
            raise ValidationError('Должно быть минимум 2 ответа')
        if len(right_answers) < 1:
            raise ValidationError('Должен быть хотя бы 1 правильный ответ')
        if len(right_answers) == len(answers):
            raise ValidationError('Все ответы не могут быть правильными')

        num_of_answers = len(answers)
        num_of_deleted_answers = sum(1 for form in self.forms if form.cleaned_data.get('DELETE', False))

        if num_of_answers - num_of_deleted_answers < 2:
            raise ValidationError('Необходимо оставить минимум 2 ответа')


class _AnswerInline(NestedTabularInline):
    extra = 0
    min_num = 2
    model = Answer
    formset = _AnswerInlineFormset
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 60})}  # Чтобы поля были менее громоздкими
    }


class _QuestionInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return

        num_of_questions = len(self.forms)
        num_of_deleted_questions = sum(1 for form in self.forms if form.cleaned_data.get('DELETE', False))

        if num_of_questions - num_of_deleted_questions < 1:
            raise ValidationError('Необходимо оставить хотя бы 1 вопрос')


class _QuestionInline(NestedStackedInline):
    extra = 0
    min_num = 1
    model = Question
    formset = _QuestionInlineFormset
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 120})}
    }
    inlines = [_AnswerInline]


@admin.register(Test)
class TestAdmin(NestedModelAdmin):
    inlines = [_QuestionInline]
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
