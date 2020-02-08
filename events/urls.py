# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('events/create/', views.create_event, name='create_event'),
]