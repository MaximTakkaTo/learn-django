# Generated by Django 3.0.5 on 2020-04-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='eng_tage',
            field=models.CharField(default=' ', max_length=200, verbose_name='Английский тэг'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='eng_tage',
            field=models.CharField(default='', max_length=200, verbose_name='Английский тэг'),
            preserve_default=False,
        ),
    ]
