# Generated by Django 3.0.5 on 2020-04-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='progress',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='study_group',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
