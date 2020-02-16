# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import (
    reverse_lazy,
)  # we use reverse_lazy to redirect the user to the login page upon successful registration
from django.views import generic

# We’re subclassing the generic class-based view CreateView in our SignUp class.
# We specify the use of the built-in UserCreationForm and the not-yet-created template at signup.html
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class LogIn(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "login.html"

