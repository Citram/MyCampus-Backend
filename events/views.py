from django.shortcuts import render, redirect
from .forms import EventForm, AddressForm
from .models import Event, Address

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


