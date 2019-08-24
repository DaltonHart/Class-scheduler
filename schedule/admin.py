from django.contrib import admin
from .models import Cohort, Schedule_Lesson, Homework_Submission
# Register your models here.

admin.site.register(Cohort)
admin.site.register(Schedule_Lesson)
admin.site.register(Homework_Submission)
