from django.contrib import admin
from .models import Course,Videos,Exams,Subjects,Readings,Assignments,Assignment_Video,Assignment_Reading,Live_Class,\
CommonExamQuestions,CommonExamAnswers
# Register your models here.

#For Courses
class SubjectVideoInline(admin.TabularInline): 
    model=Videos
class SubjectExamInline(admin.TabularInline): 
    model=Exams
class SubjectReadingInline(admin.TabularInline): 
    model=Readings
class SubjectAdmin(admin.ModelAdmin):
    inlines=[
        SubjectVideoInline,
        SubjectReadingInline,
        SubjectExamInline
    ]
#For assignments
class AssignmentVideoInline(admin.TabularInline): 
    model = Assignment_Video

class AssignmentReadingInline(admin.TabularInline): 
    model = Assignment_Reading
class AssignmentAdmin(admin.ModelAdmin):
    inlines=[
        AssignmentVideoInline,
        AssignmentReadingInline,
    ]
#For common exam
class CommonAnswerInLine(admin.TabularInline):
    model=CommonExamAnswers
class CommonExamAdmin(admin.ModelAdmin):
    inlines=[
        CommonAnswerInLine,
    ]
admin.site.register(Course)
admin.site.register(Subjects,SubjectAdmin)
admin.site.register(Assignments,AssignmentAdmin)
admin.site.register(Live_Class)
admin.site.register(CommonExamQuestions,CommonExamAdmin)

