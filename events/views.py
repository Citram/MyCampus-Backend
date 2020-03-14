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
            form_event.user_id = request.user.id
            form_event.save()
            return redirect('/')
    else:
         form_event = EventForm()
         form_address = AddressForm()
    return render(request,
                  'events/create.html',
                  {
                      'event_form': form_event,
                      'address_form': form_address
                  })

def edit_event(request):
    if request.method == 'POST':
            event_id = request.POST.get("eventid", "")
            name_input = request.POST.get("eventname", "")
            datetime_input = request.POST.get("eventdate", "")
            fee_input = request.POST.get("eventkeywords", "")
            description_input = request.POST.get("eventdescription", "")

            try :
                services.editFinal_event(event_id, name_input, datetime_input, fee_input, description_input)
            except services.UnsuccessfulOperationError:
                return HttpResponse("Event ID not valid.")
            
            return redirect('/')

    else:
        return redirect('/')

def join_event(request):
    if request.method == 'POST':
            # user_id = request.POST.get("user_id", "")
            # user_id = request.session['user']
            event_id = request.POST.get("id_field", "")
            try :
                # services.join_Finalevent(event_id, user_id)
                services.join_Finalevent(event_id)
            except services.UnsuccessfulOperationError:
                return HttpResponse("Event ID not valid.")
            
            return redirect('/')

    else:
        return redirect('/')

def leave_event(request):
    if request.method == 'POST':
            # current_user = request.session['user'] 
            # user_id = current_user.id
            user_id = request.POST.get("user_id", "")
            event_id = request.POST.get("event_id", "")
            try :
                services.leave_event(user_id, event_id)
            except ObjectDoesNotExist as error:
                return HttpResponse(error)
            
            return redirect('/')

    else:
        return redirect('/')

def edit_event_2(request):
    if request.method == 'POST':
        form_event = EventForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_event.is_valid() and form_address.is_valid():
            form_address = form_address.save()
            form_event = form_event.save(commit=False)
            form_event.address = form_address
            form_event.save()
            return redirect('/')
    else:
        event_id = request.GET.get('eventid','')
        try:
            event = services.get_event_by_id(event_id)
        except services.UnsuccessfulOperationError as e:
            return HttpResponse(e.message)
        prefill = {
            'name' : event.name,
            'datetime' : event.datetime,
            'fee': event.fee,
            'max_capacity' : event.max_capacity,
            'min_capacity': event.min_capacity,
            'description': event.description,
            'category' : event.category
        }
        address_prefill = {
            'city' : event.address.city,
            'street' : event.address.street,
            'number' : event.address.number,
            'postalcode' : event.address.postalcode
        }
        form_event = EventForm(initial=prefill)
        form_address = AddressForm(inital=address_prefill)
        return render(
            request,
            'events/edit.html',
            {
                'event_form': form_event,
                'address_form': form_address
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
            
            return redirect('/')
       
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

def get_all_events(request):

    data_dbs =  Event.objects.all()
    user = request.user.id
    event_per_user = Event.objects.filter(user_id = user)
    data_out = {'data_dbs': data_dbs, 'user_events' : event_per_user}     
    return render(request, 'home.html', data_out)

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
    if request.method == 'GET':
        pass
    else: 
        pass