from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return HttpResponse("You are home")
