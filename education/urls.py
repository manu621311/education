from django.urls import path
from .views import HomePageView,AssignmentListView,\
    CourseListAPIView,CourseDetailAPIView,TestView,\
    Request_Count,Request_Assign_Count

urlpatterns=[
    path('test/',TestView.as_view()),

    path('apiviews/<int:pk>/',CourseDetailAPIView.as_view()),
    path('apiviews/',CourseListAPIView.as_view()),

    path('',HomePageView.as_view(),name='home'),
    path('assignment/',AssignmentListView.as_view(),name='assignment'),
    
    path('request_count/',Request_Count,name='request_count'),
    path('request_assign_count/',Request_Assign_Count),
]
