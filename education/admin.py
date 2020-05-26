from django.contrib import admin
from .models import Course,Videos,Exams,Subjects,Assignments,Assignment_Video,Assignment_Reading,Live_Class
# Register your models here.
class AssignmentVideoInline(admin.TabularInline): 
    model = Assignment_Video

class AssignmentReadingInline(admin.TabularInline): 
    model = Assignment_Reading
class AssignmentAdmin(admin.ModelAdmin):
    inlines=[
        AssignmentVideoInline,
        AssignmentReadingInline,
    ]

admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(Exams)
admin.site.register(Subjects)
admin.site.register(Assignments,AssignmentAdmin)
admin.site.register(Live_Class)

