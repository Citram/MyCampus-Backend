from behave import *
from events.features.steps.create_new_event import create_events, save_events
from events.services import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from events.models import Event, Address
from django.contrib.auth import authenticate
import time
from datetime import date
import random
import string

# Set date to constant to ensure unit tests pass in future
test_date = datetime.date(2020, 2, 29)
test_date2 = datetime.date(2023, 2, 28)
client = None
error = None


@given(u'the following events are in the system')
def step_impl(context):
    events, addresses = create_events(context, True)
    save_events(events, addresses)

@given(u'Student "{username}" is logged in with password "{password}"')
def step_impl(context, username, password):
    global client
    user = {}
    user['username'] = username
    user['password1'] = password
    user['password2'] = password
    user_form = UserCreationForm(user)
    print(user_form.errors)
    assert user_form.is_valid()
    if (user_form.is_valid()):
        user_form.save()
    user = authenticate(username=username, password=password)
    assert user is not None
    client = user

@when(u'the student requests to join event "{evt_name}"')
def step_impl(context, evt_name):
    global error
    try:
        event = get_event_by_name_test(evt_name)
        if event is not None and evt_name == 'C++ Workshop':
            join_event(client.id, event.id, date=test_date2)
        else:
            join_event(client.id, event.id)
    except Exception as e:
        error = str(e)

@when(u'number of attendees of the event "{evt_name}" has not reached maximum capacity')
def step_impl(context, evt_name):
    event = get_event_by_name_test(evt_name)
    assert event.attendees.count() <= event.max_capacity

@when(u'event "{evt_name}" date is after current date')
def step_impl(context, evt_name):
    event = get_event_by_name_test(evt_name)
    assert event.datetime > test_date

@when(u'event "{evt_name}" date is before current date')
def step_impl(context, evt_name):
    event = get_event_by_name_test(evt_name)
    assert event.datetime < test_date2

@then(u'student should be added to the list of event attendees of "{evt_name}"')
def step_impl(context, evt_name):
    event_details = get_event_by_name_test(evt_name).attendees.values()
    user_ids = [detail['id'] for detail in event_details]
    assert client.id in user_ids

@given(u'max capacity of "{evt_name}" has been reached')
def step_impl(context, evt_name):
    event = get_event_by_name_test(evt_name)
    for i in range(event.max_capacity):
        user = {}
        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(10))
        password = ''.join(random.choice(letters) for i in range(10))
        user['username'] = username
        user['password1'] = password
        user['password2'] = password
        user_form = UserCreationForm(user)
        print(user_form.errors)
        assert user_form.is_valid()
        if (user_form.is_valid()):
            user_form.save()
        user = authenticate(username=username, password=password)
        assert user is not None
        join_event(user.id, event.id)
    print (event.attendees.count())


@then(u'a error message "{error_msg}" is issued')
def step_impl(context, error_msg):
    assert error_msg in error
