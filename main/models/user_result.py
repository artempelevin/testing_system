from django.conf import settings
from django.db import models


class UserResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', verbose_name='Вопрос', on_delete=models.CASCADE)
    answer = models.ForeignKey('Answer', verbose_name='Ответ', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}\t|\t{self.question.text}\t|\t{self.answer}"

    class Meta:
        app_label = 'main'
        db_table = 'user_results'
        verbose_name = 'результат тестирования'
        verbose_name_plural = 'результаты тестирования'
