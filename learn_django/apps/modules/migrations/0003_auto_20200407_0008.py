# Generated by Django 3.0.5 on 2020-04-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_auto_20200406_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='eng_tage',
            new_name='eng_tag',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='eng_tage',
            new_name='eng_tag',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_text',
            field=models.TextField(verbose_name='Текст урока'),
        ),
    ]