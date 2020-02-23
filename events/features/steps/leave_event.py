from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

@when(u'the student requests to leave event "Java Workshop"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the student requests to leave event "Java Workshop"')


@then(u'student should be removed from the list of event attendees')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then student should be removed from the list of event attendees')


@then(u'request should be invalidated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then request should be invalidated')


@then(u'an error message "Event has already occurred" is issued')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message "Event has already occurred" is issued')

