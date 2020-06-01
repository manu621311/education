from django.urls import path
from .views import HomePageView,AssignmentListView,LiveListView,CourseDetailView,SubjectDetailView,\
    CourseListAPIView,CourseDetailAPIView,TestView,\
    Request_Count,Request_Assign_Count,Request_Live_List

urlpatterns=[
    path('test/',TestView.as_view()),

    path('apiviews/<int:pk>/',CourseDetailAPIView.as_view()),
    path('apiviews/',CourseListAPIView.as_view()),

    path('',HomePageView.as_view(),name='home'),
    path('course/<int:pk>/',CourseDetailView.as_view(),name='course_detail'),
    path('subject/<int:pk>/',SubjectDetailView.as_view(),name='subject'),
    path('assignment/',AssignmentListView.as_view(),name='assignment'),
    path('live_class/',LiveListView.as_view(),name='live_classes'),
    
    path('request_count/',Request_Count,name='request_count'),
    path('request_assign_count/',Request_Assign_Count),
    path('request_live_list/',Request_Live_List),
]
