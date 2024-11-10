# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_resume/', views.add_resume, name='ui_resume_form'),
]