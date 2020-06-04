from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course,Exams,Subjects,Videos,Assignments,Assignment_Video,Assignment_Reading,Live_Class,\
    CommonExamAnswers,CommonExamQuestions
from django.http import HttpResponse
from rest_framework import generics
from .serializers import CourseSerializer,QuesAnsSerializer
import json
# Create your views here.
#some extra initialization

class HomePageView(LoginRequiredMixin,ListView):
    template_name='home.html'
    model=Course
    context_object_name='course'
    login_url='login'
class CourseDetailView(LoginRequiredMixin,DetailView):
    template_name='course_detail.html'
    model=Course
    context_object_name='course'
    login_url='login'
    def get_context_data(self, **kwargs):#To pass extra data
        subject=Subjects.objects.all()
        context = super().get_context_data(**kwargs)
        context['subject'] = subject
        return context
class SubjectDetailView(LoginRequiredMixin,DetailView):
    template_name='subject.html'
    model=Subjects
    context_object_name='subject'
    login_url='login'
#Common Exam
class CommonExamView(LoginRequiredMixin,ListView):
    template_name='common_exam.html'
    model=CommonExamQuestions
    login_url='login'
    context_object_name='questions'
#Assignment classes
class AssignmentListView(LoginRequiredMixin,ListView):
    template_name='assignments_list.html'
    model=Course
    context_object_name='course'
    login_url='login'
#Live classes
class LiveListView(LoginRequiredMixin,ListView):
    template_name='live_list.html'
    model=Live_Class
    context_object_name='liveclass'
    login_url='login'
#APIs
class CourseListAPIView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
class QueAnsAPIView(generics.ListCreateAPIView):
    queryset=CommonExamQuestions.objects.all()
    serializer_class=QuesAnsSerializer
class TestView(TemplateView):
    template_name='test.html'
#Request Functions
def Request_Count(request):
    exam_count,subject_count,video_count,progress,count_dict=[],[],[],[],{}
    a=Course.objects.all()
    for i in range(0,a.count()):
        sum1,sum2=0,0
        subject_count.append(a[i].subjects.count())
        x=a[i].subjects.all()
        for j in range(0,a[i].subjects.count()):
            sum1+=x[j].videos.count()
            sum2+=x[j].exams.count()
        video_count.append(sum1)
        exam_count.append(sum2)
        progress.append(a[i].course_progress)
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
def Request_Question_Answer(request):
    dict,ques,ans={},{},[]
    a=CommonExamQuestions.objects.all()
    for i in range(0,a.count()):
    #    ques.append(a[i].question)
        c=a[i].answer.all()
        for j in c[i]:
            pass
        ques[a[i].question]=ans
    dict['ques']=ques
    return HttpResponse(json.dumps(dict))


    

