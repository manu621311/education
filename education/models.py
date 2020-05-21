from django.db import models
from django.urls import reverse
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=150)
    course_progress=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.course_name
class Videos(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='videos')
    videos= models.FileField(upload_to='videos/', null=True)
class Exams(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='exams')
    exams= models.CharField(max_length=150)
class Subjects(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subjects')
    subjects= models.CharField(max_length=150)