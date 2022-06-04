from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # start a task
    return HttpResponse("<h1>Гружу кота!!!</h1>")

