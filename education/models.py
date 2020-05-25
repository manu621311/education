from django.db import models
from django.urls import reverse
# Create your models here.
choice=(('1','Done'),('2','Not Done'))

class Course(models.Model):
    course_name=models.CharField(max_length=150)
    course_progress=models.IntegerField(null=True,blank=False)
    def __str__(self):
        return self.course_name
class Videos(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='videos')
    videos= models.FileField(upload_to='videos/', null=True,verbose_name='video')
    def __str__(self):
        return str(self.course)
class Exams(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='exams')
    exams= models.CharField(max_length=150,verbose_name='exam')
    def __str__(self):
        return str(self.course)
class Subjects(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subjects')
    subjects= models.CharField(max_length=150,verbose_name='subject')
    def __str__(self):
        return str(self.course)
class Assignments(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='assignments')
    assignment_progress=models.IntegerField(null=True,blank=False)
    assignment_deadline=models.DateTimeField(auto_now_add=False)
    assignment_status=models.CharField(max_length=20,choices=choice,blank=False,verbose_name='Mark as',default=choice[1])
    def __str__(self):
        return str(self.course)
    
class Assignment_Video(models.Model):
    assignment=models.ForeignKey(
        Assignments,
        on_delete=models.CASCADE,
        related_name='assignment_video'
    )
    assignment_video=models.FileField(upload_to='videos/', null=True,blank=True,verbose_name='video')
class Assignment_Reading(models.Model):
    assignment=models.ForeignKey(
        Assignments,
        on_delete=models.CASCADE,
        related_name='assignment_reading'
    )
    assignment_reading=models.FileField(upload_to='PDF/',null=True,blank=True,verbose_name='reading_material')
