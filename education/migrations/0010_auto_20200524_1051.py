# Generated by Django 3.0 on 2020-05-24 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_assignments_assignment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='assignment_content',
        ),
        migrations.RemoveField(
            model_name='assignments',
            name='assignment_video',
        ),
        migrations.CreateModel(
            name='Assignment_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_video', models.FileField(null=True, upload_to='videos/', verbose_name='video')),
                ('assignment_reading', models.FileField(null=True, upload_to='PDF/', verbose_name='reading_material')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_videos', to='education.Assignments')),
            ],
        ),
    ]