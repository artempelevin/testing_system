from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Тема теста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'main'
        db_table = 'tests'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
