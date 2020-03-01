from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

@when(u'the student requests a list of events')
def step_impl(context):
    global g_exception
    try:
        event = Event.objects.all()
    except Exception as e:
        g_exception = e
@then(u'the following list of events is generated')
def step_impl(context):
    pass
    

@when(u'the student requests a list of events with the keyword "{workshop}"')
def step_impl(context, workshop):
    global g_exception
    try: 
        get_events_by_words_in_name(workshop)
    except Exception as e:
        g_exception = e

@then(u'an error message "No events available for keyword: cat" should be issued')
def step_impl(context):
    global g_exception
    #assert error in str(g_exception)
    #raise NotImplementedError(u'STEP: Then an error message "No events available for keyword: cat" should be issued')


