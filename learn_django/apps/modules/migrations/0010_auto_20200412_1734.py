# Generated by Django 3.0.5 on 2020-04-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_auto_20200412_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('lesson_id',), 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
