from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

g_exception = None

g_addresses = None

@when(u'the student requests to edit event {id_element} with name {name}')
def step_impl(step, id_element, name):
    global g_exception
    try:
        event = Event.objects.get(id=id_element)
        editFinal_event(id_element, name,  event.datetime,  event.fee, event.description)
    except Exception as e:
        g_exception = e
    #raise NotImplementedError(u'STEP: When the student requests to edit event JavaWorkshop')


@then(u'the event with name {name} should be updated with its new fields and stored in the system')
def step_impl(step, name):
    events = Event.objects.all()
    pass
    #raise NotImplementedError(u'STEP: Then the event with name JavaWorkshop should be updated with its new fields and stored in the system')


@when(u'the student requests to edit an existing {id_element} without specifying at least one field an {error} is shown' )
def step_impl(context, id_element, error):
    global g_exception
    try:
        event = Event.objects.get(id=id_element)
        editFinal_event(id_element, null, event.datetime,  event.fee, event.description)
    except Exception as e:
        pass

    #raise NotImplementedError(u'STEP: When the student requests to edit an existing event without specifying at least one field')

@when(u'the student requests to edit an {id_element} with at least one {invalid} field')
def step_impl(context, id_element, invalid):
    global g_exception
    try:
        event = Event.objects.get(id=id_element)
        editFinal_event(id_element, invalid, event.datetime,  event.fee, event.description)
    except Exception as e:
        pass

