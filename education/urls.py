from django.urls import path
from .views import HomePageView,Request_count

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('request_count/',Request_Count,name='request_count')
]
