# Generated by Django 3.0.5 on 2020-04-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_module_module_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='eng_tag',
            field=models.CharField(max_length=200, verbose_name='Английский тег'),
        ),
    ]