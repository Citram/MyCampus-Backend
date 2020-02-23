from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from create_new_event import create_events, save_events
from events.services import delete_event_by_name

@when(u'the student requests to edit event JavaWorkshop')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the student requests to edit event JavaWorkshop')


@then(u'the event with name JavaWorkshop should be updated with its new fields and stored in the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the event with name JavaWorkshop should be updated with its new fields and stored in the system')


@when(u'the student requests to edit an existing event without specifying at least one field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the student requests to edit an existing event without specifying at least one field')


@when(u'the student requests to edit an event with at least one invalid field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the student requests to edit an event with at least one invalid field')


