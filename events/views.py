from django.shortcuts import render, redirect
from .forms import EventForm, AddressForm
from .models import Event, Address
from django.http import Http404, HttpResponse
from events.forms import DeleteEventForm

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
            try:
                Event.objects.get(id=id_field).delete()
            except:
                return HttpResponse("Event with id " + id_field + " not found.")
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


