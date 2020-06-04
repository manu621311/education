from django.db import models
from django.urls import reverse
# Create your models here.
choice1=(('1','Done'),('2','Not Done'))
choice2=(('Video','Video'),('PDF','PDF'))
#Regular Course section
class Course(models.Model):
    course_name=models.CharField(max_length=150)
    course_progress=models.IntegerField(null=True,blank=False)
    def __str__(self):
        return self.course_name
    def get_absolute_url(self): # new 
        return reverse('course_detail', args=[str(self.pk)])
class Subjects(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subjects')
    subjects= models.CharField(max_length=150,verbose_name='subject',null=False)
    subject_info=models.CharField(max_length=150,blank=False,null=False,default="It is the medium in which objects and subjects actually come into existence, and is the medium in which their virtuality resides.\
This book is an introduction to logic, as contemporary logicians now understand the subject.")
    def __str__(self):
        return str(self.course)
    
class Videos(models.Model):
    subject=models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE,
        related_name='videos')
    videos= models.FileField(upload_to='videos/', null=True,verbose_name='video',default='')
    video_info=models.CharField(max_length=500,verbose_name='Info',null=False,default='')
    def __str__(self):
        return str(self.subject)
class Exams(models.Model):
    subject=models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE,
        related_name='exams')
    exams= models.CharField(max_length=150,verbose_name='exam',null=True,default='')
    def __str__(self):
        return str(self.subject)
class Readings(models.Model):
    subject=models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE,
        related_name='readings')
    readings= models.FileField(upload_to='PDF/', null=True,verbose_name='content')
    reading_info= models.CharField(max_length=500,verbose_name='Info',null=False,default='')
    def __str__(self):
        return str(self.subject)
#Assignments section
class Assignments(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='assignments')
    assignment_progress=models.IntegerField(null=True,blank=False)
    assignment_deadline=models.DateTimeField(auto_now_add=False)
    assignment_status=models.CharField(max_length=20,choices=choice1,blank=False,verbose_name='Mark as',default=choice1[1])
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
#Live Class Section     
class Live_Class(models.Model):
    course=course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='live_class')
    topic=models.CharField(max_length=20,blank=False,default='topic_name')
    scheduled_time=models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return str(self.course)
#For exam
class CommonExamQuestions(models.Model):
    question=models.CharField(max_length=200)
    def __str__(self):
        return str(self.question)    
class CommonExamAnswers(models.Model):
    question=models.ForeignKey(
        CommonExamQuestions,
        on_delete=models.CASCADE,
        related_name='answer'
    )
    answer=models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        x=[]
        x.append(self.answer)
        x.append(self.is_correct)
        return str(x)



