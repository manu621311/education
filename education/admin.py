from django.contrib import admin
from .models import Course,Videos,Exams,Subjects
# Register your models here.
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(Exams)
admin.site.register(Subjects)

