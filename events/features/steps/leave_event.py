from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address
from events.features.steps.create_new_event import create_events, save_events
import time
from datetime import date
import random
import string
from events.services import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Set date to constant to ensure unit tests pass in future
test_date = datetime.date(2020, 2, 29)
test_date2 = datetime.date(2023, 2, 28)
client = None
error = None
g_event = None

@given(u'the events are in the system')
def step_impl(context):
    events, addresses = create_events(context, True)
    save_events(events, addresses)

@given(u'"{username}" is logged in with password "{password}"')
def step_impl(context, username, password):
    global client
    user = {}
    user['username'] = username
    user['password1'] = password
    user['password2'] = password
    user_form = UserCreationForm(user)
    assert user_form.is_valid()
    if (user_form.is_valid()):
        user_form.save()
    user = authenticate(username=username, password=password)
    assert user is not None
    client = user

@given(u'student is an attendee of the event "{evt_name}"')
def step_impl(context, evt_name):
    global client
    event = get_event_by_name_test(evt_name)
    join_event(client.id, event.id)

@given(u'student is not an attendee of the event "Java Workshop"')
def step_impl(context):
    global g_event
    global client
    event_details = g_event.attendees.values()
    user_ids = [detail['id'] for detail in event_details]
    assert client.id not in user_ids

@when(u'the student requests to leave event "{evt_name}"')
def step_impl(step, evt_name):
    global g_event
    global client
    global error
    try:
        g_event = get_event_by_name_test(evt_name)
        if g_event is not None and evt_name == 'C++ Workshop':
            leave_event(client.id, g_event.id, date=test_date2)
        else:
            leave_event(client.id, g_event.id)
    except Exception as e:
        error = str(e)
        print(error)

@then(u'student should be removed from the list of event attendees')
def step_impl(context):
    global g_event
    global client
    event_details = g_event.attendees.values()
    user_ids = [detail['id'] for detail in event_details]
    assert client.id not in user_ids


@when(u'event date is after current date')
def step_impl(context):
    global g_event
    assert g_event.datetime > test_date

@when(u'event date is before current date')
def step_impl(context):
    global g_event
    assert g_event.datetime < test_date2


@then(u'an error message "{error_msg}" is given')
def step_impl(context, error_msg):
    global error
    print(error)
    print(error_msg)
    assert error_msg in error