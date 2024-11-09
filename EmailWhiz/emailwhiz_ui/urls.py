from django.urls import path
from . import views

urlpatterns = [
    path('add_resume/', views.add_resume, name='resume_form'),
    path('login/', views.login_view, name='login'),
]
