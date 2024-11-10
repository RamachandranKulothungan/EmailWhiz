from django.urls import path
from . import views

urlpatterns = [
    path('save_resume/', views.save_resume, name='save_resume'),
    path('send_emails/', views.send_emails, name='send_emails'),
    path('generate_emails/', views.generate_emails, name='generate_emails'),

]

