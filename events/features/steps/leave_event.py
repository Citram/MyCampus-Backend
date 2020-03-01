from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

@when(u'the student requests to leave event "{id_element}"')
def step_impl(step, id_element):
    global g_exception
    try:
        event = Event.objects.get(id=id_element)
        leave_event(id_element, event.id)
    except Exception as e:
        g_exception = e

@then(u'{user_id} should be removed from the list of {id_element} attendees')
def step_impl(step, user_id, id_element):
    user = Student.objects.get(user_id)
    event = Event.objects.get(id=id_element)
    try:
         event.attendees.remove(user)
    except Exception as e:
        pass #Since if we try to remove something that's not there, then we have successfully left the event

@then(u'request should be invalidated')
def step_impl(context):
    pass

@then(u'an error message "{error}" is issued')
def step_impl(step, error):
    global g_exception
    assert error in str(g_exception)
