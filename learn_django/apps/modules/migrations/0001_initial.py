# Generated by Django 3.0.5 on 2020-04-06 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_title', models.CharField(max_length=200, verbose_name='Название модуля')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=200, verbose_name='Название урока')),
                ('lesson_text', models.TextField(verbose_name='Текст статьи')),
                ('lesson_pub_date', models.DateField(verbose_name='Дата публикации')),
                ('Module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Module')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
