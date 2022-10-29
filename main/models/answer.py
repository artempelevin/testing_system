from django.db import models


class Answer(models.Model):
    text = models.TextField(null=False, verbose_name='Тест ответа')
    is_right = models.BooleanField(null=False, default=False, verbose_name='Это правильный ответ?')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'main'
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
