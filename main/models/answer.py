from django.db import models


class Answer(models.Model):
    text = models.TextField(null=False, verbose_name='Текст ответа')
    is_right = models.BooleanField(null=False, default=False, verbose_name='Это правильный ответ?')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'main'
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return self.text if len(self.text) < 35 else f"{self.text[:32]}..."
