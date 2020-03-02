# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("events/create/", views.create_event, name="create_event"),
    path("events/delete/", views.delete_event, name="delete_event"),
    path("events/edit/", views.edit_event, name="editevents"),
    path("", views.get_all_events, name="getallevents"),
    path("events/register/<>", views.register_for_event, name="register_for_event",),
]
