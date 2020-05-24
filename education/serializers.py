from rest_framework import serializers
from .models import Course,Videos,Exams,Subjects

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Course


