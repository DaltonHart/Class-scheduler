from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

CHOICES = (("MORNING", "9-10"), ("MORNING_2", "1015-1230"), ("AFTERNOON",
                                                             "130-3"), ("AFTERNOON2", "315-5"), ("HOMEWORK", "HOMEWORK"))
DAY_CHOICES = (("MONDAY", "Monday"), ("TUESDAY", "Tuesday"), ("WEDNESDAY",
                                                              "Wednesday"), ("THURSDAY", "Thursday"), ("FRIDAY", "Friday"))


class Cohort(models.Model):
    type = models.CharField(max_length=20)
    number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.number}"


class Schedule_Lesson(models.Model):
    week = models.IntegerField()
    day = models.CharField(choices=DAY_CHOICES, max_length=20)
    slot = models.CharField(choices=CHOICES, max_length=20)
    cohort = models.ForeignKey(
        'Cohort', on_delete=models.CASCADE, related_name='schedule_items')
    lesson_url = models.URLField()
    lesson_title = models.CharField(max_length=20)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.lesson_title} - {self.cohort}"


class Homework_Submission(models.Model):
    lesson = models.ForeignKey(
        'Schedule_Lesson', on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='submissions')
    url = models.URLField()
    grade = models.BooleanField()
    end_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.lesson} - {self.user}"
