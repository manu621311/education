from rest_framework import serializers
from .models import Course,Videos,Exams,Subjects,CommonExamQuestions,CommonExamAnswers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Course
class QuesAnsSerializer(serializers.ModelSerializer):
    answer=serializers.StringRelatedField(many=True)
    class Meta:
        fields=['id','question','answer']
        model=CommonExamQuestions
        

