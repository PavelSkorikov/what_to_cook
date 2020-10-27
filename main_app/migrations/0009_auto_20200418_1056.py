# Generated by Django 3.0.5 on 2020-04-18 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_auto_20200417_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, verbose_name='Дизлайки'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.IntegerField(blank=True, default=0, verbose_name='Лайки'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(default=None, max_length=5000, verbose_name='Комментарий к рецепту')),
                ('createAt', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Recipe', verbose_name='рецепт')),
                ('user', models.ForeignKey(on_delete=models.SET('anonimous_user'), to=settings.AUTH_USER_MODEL, verbose_name='автор комментария')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коменетарии',
                'ordering': ['createAt'],
            },
        ),
    ]