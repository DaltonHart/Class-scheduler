from django.db import models

from django.contrib.auth.models import User
from schedule.models import Cohort
# Create your models here.


class Profile(models.Model):
    github = models.URLField()
    instructor = models.BooleanField()
    avatar = models.TextField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
