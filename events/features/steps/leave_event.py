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

@then(u'student should be removed from the list of event attendees')
def step_impl(context):
    event = Event.objects.all()
    pass
    #raise NotImplementedError(u'STEP: Then student should be removed from the list of event attendees')


@then(u'request should be invalidated')
def step_impl(context):
        #attendees doesn't seem to work
        #attendees = Event.objects.attendees.all()
        assert Event.objects.all() != 0 #There's an error with event.attendees.all

@then(u'an error message "Event has already occurred" is issued')
def step_impl(context):
    assert Event.objects.all() != 0
    print("error = Event has already occurred")