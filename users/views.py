# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #we use reverse_lazy to redirect the user to the login page upon successful registration
from django.views import generic
from .forms import *
from . import services
from events.services import UnsuccessfulOperationError
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions.backends.base import SessionBase
# We’re subclassing the generic class-based view CreateView in our SignUp class.
# We specify the use of the built-in UserCreationForm and the not-yet-created template at signup.html
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['passwrod']
                try :
                    success = services.login(username, password)
                    if success:
                        request.session['id'] = username
                        return redirect('dashboard')
                except UnsuccessfulOperationError as e:
                    return HttpResponse(e.message)
        else:
            login_form = LoginForm()
            return render(
                'users/login.html',
                {'login_form': login_form} 
            )
    #SEE:
    #https://stackoverflow.com/questions/14465993/how-can-i-set-and-get-session-variable-in-django
    #https://django-book.readthedocs.io/en/latest/chapter14.html

def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            id = student_form.cleaned_data['id']
            password = student_form.cleaned_data['password']
            email = student_form.cleaned_data['email']
            name = student_form.cleaned_data['name']
            description = student_form.cleaned_data['description']
            age = student_form.cleaned_data['age']
            gender = student_form.cleaned_data['gender']
            faculty = student_form.cleaned_data['faculty']
            try:
                services.create_student(id, password, email, name, description, age, gender, faculty)
            except UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
        return redirect('dashboard') #TODO: return to dashboard????
    else:
        student_form = StudentForm()
        return render(
            request,
            'users/create.html',
            {'student_form': student_form}
        )

def create_admin(request):
    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        if admin_form.is_valid():
            id = admin_form.cleaned_data['id']
            password = admin_form.cleaned_data['password']
            email = admin_form.cleaned_data['email']
            try:
                services.create_admin(id, password, email)
            except UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
        return redirect('dashboard') #TODO: return to dashboard????
    else:
        admin_form = AdminForm()
        return render(
            request,
            'users/create.html',
            {'admin_form': admin_form}
        )

def create_organization(request):
    if request.method == 'POST':
        org_form = OrganizationForm(request.POST)
        if org_form.is_valid():
            id = org_form.cleaned_data['id']
            password = org_form.cleaned_data['password']
            email = org_form.cleaned_data['email']
            name = org_form.cleaned_data['name']
            description = org_form.cleaned_data['description']
            try:
                services.create_organization(id, password, email, name, description)
            except UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
            return redirect('dashboard') #TODO: return to dashboard????
    else:
        org_form = OrganizationForm()
        return render(
            request,
            'users/create.html',
            {'org_form': org_form}
        )

def create_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            user_id = request.session['id'] #TODO: check
            event_id = review_form.data['event']
            rating = review_form.data['rating']
            comment = review_form.data['comment']
            try:
                services.create_review(user_id,event_id, rating, comment)
            except UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
            return redirect('users/review') #TODO
    else:
        review_form = ReviewForm()
        return render(
            request,
            'users/review.html', #TODO
            {'review_form' : review_form}
        )

def delete_review(request):
    if request.method == 'POST':
        user_id = request.session['id'] #TODO: check
        review_id = request.cleaned_data['review_id']
        try:
            services.delete_review(user_id, review_id)
        except services.UnsuccessfulOperationError:
            return HttpResponse("Delete ID not valid.")
            
        return HttpResponse("Review deleted.")
    else:
        return redirect('reviews') #TODO
