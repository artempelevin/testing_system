# Generated by Django 4.1.2 on 2022-10-30 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема теста')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 'tests',
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.test'),
            preserve_default=False,
        ),
    ]
