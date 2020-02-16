from django.shortcuts import render, redirect
from .forms import EventForm, AddressForm, CommentForm
from .models import Event, Address
from users import models as user_models
from django.http import Http404, HttpResponse
from events.forms import DeleteEventForm, RegistrationForm
from django.core.exceptions import ObjectDoesNotExist
from . import services

# Create your views here.
def create_event(request):
    if request.method == 'POST':
        form_event = EventForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_event.is_valid() and form_address.is_valid():
            form_address = form_address.save()
            form_event = form_event.save(commit=False)
            form_event.address = form_address
            form_event.save()
            return redirect('create_event')
    else:
        event_form = EventForm()
        address_form = AddressForm()
    return render(request,
                  'events/create.html',
                  {
                      'event_form': event_form,
                      'address_form': address_form
                  })

def delete_event(request):
    if request.method == 'POST':
        delete_form = DeleteEventForm(request.POST)
        if delete_form.is_valid():
            id_field = delete_form.data['id_field']

            try :
                services.delete_event(id_field)
            except services.UnsuccessfulOperationError:
                return HttpResponse("Delete ID not valid.")
            
            return HttpResponse("Event deleted.")
       
        # try:
        #     id = request.POST.get('id', '')
        # except:
        #     return HttpResponse("Error: ID of event to delete must be specified."
    else:
        delete_form = DeleteEventForm()
        return render(request, 'events/delete.html',
                {
                    'delete_form': delete_form
                })


def register_for_event(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            current_user = request.session['id'] #TODO: check
            user_id = current_user.id
            event_id = registration_form.data['event_id'] 
            try:
                services.join_event(user_id, event_id)
                return HttpResponse("Successfully joined the event.")
            except services.UnsuccessfulOperationError as e:
                return HttpResponse(e.message)
    else:
        registration_form = RegistrationForm()
        return render(
            request, 
            'events/register.html', 
            {'registration_form': registration_form}
        )

def create_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            current_user = request.session['id'] 
            user_id = current_user.id
            event_id = comment_form.data['event_id'] 
            try:
                services.create_comment(event_id,user_id,comment_form.data['message'])
            except ObjectDoesNotExist as error:
                return HttpResponse(error)
    else:
        comment_form = CommentForm()
        return render(
            request,
            {'comment_form': comment_form}
        )
        
def query_event_by_category(request):
