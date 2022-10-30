from django.contrib import admin
from django.db import models
from django.forms import Textarea
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin

from main.forms import TestForm
from main.models import Test, Question, Answer


class _AnswerInline(NestedTabularInline):
    extra = 0
    min_num = 2
    model = Answer
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 60})}  # Чтобы поля были менее громоздкими
    }


class _QuestionInline(NestedStackedInline):
    extra = 0
    min_num = 1
    model = Question
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 120})}
    }
    inlines = (_AnswerInline,)


class TestAdmin(NestedModelAdmin):
    model = Test
    form = TestForm
    inlines = (_QuestionInline,)
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-updated_at', )


admin.site.register(Test, TestAdmin)
