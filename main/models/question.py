from django.db import models


class Question(models.Model):
    text = models.TextField(null=False, verbose_name='Тест вопроса')

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'main'
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
