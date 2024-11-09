from django.urls import path
from . import views

urlpatterns = [
    path('add_resume/', views, name='view1'),
    # Add more URL patterns as needed
]