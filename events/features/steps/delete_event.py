from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

g_exception = None

@given(u'the following events exist in the database')
def step_impl(context):
        events, addresses = create_events(context, True)
        save_events(events, addresses)
        
@when(u'the student requests to delete event {name}')
def step_impl(step, name):
    global g_exception
    try:
        delete_event_by_name(name)
    except Exception as e:
        g_exception = e
    

@then(u'the event should with name {name} should be deleted from the system')
def step_impl(context, name):
    events = Event.objects.all()
    for event in events:
        assert event.name != name

@then(u'the error message "{error}" should be issued')
def step_impl(context, error):
    global g_exception
    assert error in str(g_exception)