# Generated by Django 3.0 on 2020-05-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20200520_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_progress',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
