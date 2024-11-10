from django.urls import path
from . import views

urlpatterns = [
    path('add_resume/', views.add_resume, name='ui_resume_form'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]