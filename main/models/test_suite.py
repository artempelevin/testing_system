from django.db import models


class TestSuite(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'main'
        db_table = 'test_suites'
        verbose_name = 'набор тестов'
        verbose_name_plural = 'наборы тестов'


def provide_default_test_suite() -> int:
    default_test_suite, _ = TestSuite.objects.get_or_create(name='Стандартный набор тестов')
    return default_test_suite.id
