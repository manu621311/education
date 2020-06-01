# Generated by Django 3.0 on 2020-06-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200531_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='subject_info',
            field=models.CharField(default='It is the medium in which objects and subjects actually come into existence, and is the medium in which their virtuality resides.This book is an introduction to logic, as contemporary logicians now understand the subject.', max_length=150),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_info',
            field=models.CharField(default='', max_length=500, verbose_name='Info'),
        ),
    ]
