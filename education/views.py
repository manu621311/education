from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course,Exams,Subjects,Videos
from django.http import HttpResponse
from rest_framework import generics
from .serializers import CourseSerializer
import json
# Create your views here.
#some extra initialization

class HomePageView(LoginRequiredMixin,ListView):
    template_name='home.html'
    model=Course
    context_object_name='course'
    login_url='login'

class CourseListAPIView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
class TestView(TemplateView):
    template_name='test.html'

def Request_Count(request):
    exam_count,subject_count,video_count,progress,count_dict=[],[],[],[],{}
    a=Course.objects.all()
    for i in range(0,a.count()):
        progress.append(a[i].course_progress)
        exam_count.append(a[i].exams.count())
        subject_count.append(a[i].subjects.count())
        video_count.append(a[i].videos.count())
    count_dict['exam_count']=exam_count
    count_dict['subject_count']=subject_count
    count_dict['video_count']=video_count
    count_dict['progress']=progress
    return HttpResponse(json.dumps(count_dict))
    

