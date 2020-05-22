from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course,Exams,Subjects,Videos
import json
# Create your views here.
#some extra initialization

class HomePageView(LoginRequiredMixin,ListView):
    template_name='home.html'
    model=Course
    context_object_name='course'
    login_url='login'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #some extra initialization
        exam_count,subject_count,video_count,progress=[],[],[],[]
        a=Course.objects.all()
        for i in range(0,a.count()):
            progress.append(a[i].course_progress)
            exam_count.append(a[i].exams.count())
            subject_count.append(a[i].subjects.count())
            video_count.append(a[i].videos.count())

        context['exam_count'],context['subject_count'],context['video_count'],context['progress']=\
        json.dumps(exam_count),subject_count,video_count,progress
        return context



