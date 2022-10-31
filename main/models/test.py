from django.db import models

from main.models.test_suite import provide_default_test_suite


class Test(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Тема теста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    test_suite = models.ForeignKey('TestSuite', verbose_name='Набор тестов',
                                   default=provide_default_test_suite, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'main'
        db_table = 'tests'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
