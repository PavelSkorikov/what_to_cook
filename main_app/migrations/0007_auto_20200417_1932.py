# Generated by Django 3.0.5 on 2020-04-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200417_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='complexity',
            field=models.CharField(blank=True, choices=[('EASY', 'Простой'), ('MIDLE', 'Средний'), ('HARD', 'Сложный'), ('SUPER_HARD', 'Очень сложный')], default='Простой', max_length=50, verbose_name='Сложность приготовления'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(blank=True, default='0 мин', max_length=50, verbose_name='Время приготовления'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(blank=True, default=1, max_length=5, verbose_name='Количество порций'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Описание'),
        ),
    ]
