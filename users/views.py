from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def users(request):
    return HttpResponse("Hello, world. You're at the users page.")

    #This is the function to create a session on signup
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")
    #This is the function to access the session on login. -> request.session.get('name') for the username, or id, ect from the database
def access_session(request):
    response = "<h1>Welcome to Sessions of MyCampus</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')