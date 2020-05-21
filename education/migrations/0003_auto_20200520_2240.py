# Generated by Django 3.0 on 2020-05-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200520_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.FileField(null=True, upload_to='videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='education.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='video_lectures',
        ),
    ]
