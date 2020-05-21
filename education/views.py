from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView
from .models import Course
# Create your views here.

class HomePageView(LoginRequiredMixin,ListView):
    template_name='home.html'
    model=Course
    context_object_name='lesson'
    login_url='login'
