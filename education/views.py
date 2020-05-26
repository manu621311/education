from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course,Exams,Subjects,Videos,Assignments,Assignment_Video,Assignment_Reading,Live_Class
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

class AssignmentListView(LoginRequiredMixin,ListView):
    template_name='assignments_list.html'
    model=Course
    context_object_name='course'
    login_url='login'
class LiveListView(LoginRequiredMixin,ListView):
    template_name='live_list.html'
    model=Live_Class
    context_object_name='liveclass'
    login_url='login'

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

def Request_Assign_Count(request):
    subject_name,video_count,reading_count,status,progress,deadline,count_dict=\
        [],[],[],[],[],[],{}
    a=Assignments.objects.all()
    for i in range(0,a.count()):
        subject_name.append(str(a[i].course))
        progress.append(a[i].assignment_progress)
        video_count.append(a[i].assignment_video.count())
        reading_count.append(a[i].assignment_reading.count())
        status.append(a[i].assignment_status)
        deadline.append(str(a[i].assignment_deadline))
    count_dict['subject_name']=subject_name
    count_dict['progress']=progress
    count_dict['video_count']=video_count
    count_dict['reading_count']=reading_count
    count_dict['status']=status
    count_dict['deadline']=deadline
    return HttpResponse(json.dumps(count_dict))

def Request_Live_List(request):
    subject_name,topic_name,deadline,count_dict=\
        [],[],[],{}
    a=Live_Class.objects.all()
    for i in range(0,a.count()):
        subject_name.append(str(a[i].course))
        topic_name.append(a[i].topic)
        deadline.append(str(a[i].scheduled_time))
    count_dict['subject_name']=subject_name
    count_dict['deadline']=deadline
    count_dict['topic_name']=topic_name
    return HttpResponse(json.dumps(count_dict))





    

