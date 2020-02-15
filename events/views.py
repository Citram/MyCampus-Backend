from django.shortcuts import render, redirect
from .forms import EventForm, AddressForm
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
            if services.delete_event(id_field):
                return HttpResponse("Event deleted.")
        else:
            return HttpResponse("Delete ID not valid.")
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
            current_user = request.user 
            user_id = current_user.id
            event_id = registration_form.data['event_id']
            try:
                services.join_event(user_id, event_id)
                return HttpResponse("Successfully joined the event.")
            except ObjectDoesNotExist as error:
                return HttpResponse(error)
    else:
        registration_form = registration_form()
        return render(request, 'events/register.html', {
            'registration_form': registration_form
        })
        
