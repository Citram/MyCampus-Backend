from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

# Create your views here.
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_event')
    else:
        form = EventForm()
    return render(request,
                  'events/create.html',
                  {
                      'form': form
                  })


