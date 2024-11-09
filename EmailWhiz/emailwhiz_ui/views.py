from django.shortcuts import render
from django.http import HttpResponse


def add_resume(request):
    return render(request, 'add_resume.html')
