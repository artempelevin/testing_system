from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db import models
from django.forms import Textarea

from main.forms import QuestionForm
from main.models import Question, Answer


class AnswerAdminInline(TabularInline):
    extra = 0
    model = Answer
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})}  # Чтобы поля были менее громоздкими
    }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    inlines = (AnswerAdminInline,)
