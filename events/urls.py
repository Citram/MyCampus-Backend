# accounts/urls.py
from django.urls import path

from . import views
from . import services


urlpatterns = [
    path('events/create/', views.create_event, name='create_event'),
    path('events/delete/', views.delete_event, name='delete_event'),
    path('events/join/', views.join_event, name='join_event'),
    path('events/edit/', views.edit_event, name='edit_event'),
    path('', views.get_all_events, name='getallevents'),

]