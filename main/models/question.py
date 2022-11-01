from django.db import models


class Question(models.Model):
    text = models.TextField(null=False, verbose_name='Текст вопроса')
    test = models.ForeignKey('Test', verbose_name='Тест', on_delete=models.CASCADE)

    class Meta:
        app_label = 'main'
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text
