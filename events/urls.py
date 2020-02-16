# accounts/urls.py
from django.urls import path

from . import views

category = {
    "category1": "entertainment",
    "category2": "networking",
    "category3": "educational",
    "category4": "study",
}

urlpatterns = [
    path("events/create/", views.create_event, name="create_event"),
    path("events/delete/", views.delete_event, name="delete_event"),
    path("", views.get_all_events, name="getallevents"),
    path(
        "events/category/",
        views.query_event_by_category(request=category),
        name="query_event_list",
    ),
]

