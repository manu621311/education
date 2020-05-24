from django.urls import path
from .views import HomePageView,CourseListAPIView,CourseDetailAPIView,TestView,Request_Count

urlpatterns=[
    path('apiviews/<int:pk>/',CourseDetailAPIView.as_view()),
    path('apiviews/',CourseListAPIView.as_view()),
    path('',HomePageView.as_view(),name='home'),
    path('test/',TestView.as_view()),
    path('request_count/',Request_Count,name='request_count')
]
