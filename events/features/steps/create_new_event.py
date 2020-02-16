from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address

use_step_matcher("parse")

g_events = None
g_addresses = None

@given(u'Student "{name}" is logged in')
def student_logged_in(step, name):
    pass

@when(u'the student requests to create an event')
def step_impl(context):
    events, addresses = create_events(context, True)
    save_events(events, addresses)     


@when(u'the student requests to create an event without a minimum capacity')
def step_impl(context):
    events, addresses = create_events(context, False)
    save_events(events, addresses) 

@then(u'the event should with name <evt_name> should be created and stored in the system')
def step_impl(context):
    events = Event.objects.all()
    assert len(events) == len(context.table.rows)
    
    for idx, row in enumerate(context.table):
        event = events[idx]
        assert event.name == row['evt_name']
        assert event.datetime.strftime("%Y-%m-%d") == row['evt_date']
        assert int(event.fee) == int(row['fee'])
        assert int(event.max_capacity) == int(row['max_cap'])
        assert int(event.min_capacity) == int(row['min_cap'])

        assert event.description == row['evt_details']
        assert event.category == row['category']
        
        address = event.address
        assert address.city == row['city']
        assert address.street == row['street']
        assert address.number == row['number']
        assert address.postalcode == row['postalcode']
        
@when(u'the student requests to create an event without specifying at least one field')
def step_impl(context):
    events, addresses = create_events(context, False)
    global g_addresses
    global g_events
    g_events = events
    g_addresses = addresses

@when(u'the student requests to create an event with at least one invalid field')
def step_impl(context):
    events, addresses = create_events(context, True)
    global g_addresses
    global g_events
    g_events = events
    g_addresses = addresses


@then(u'the request should be invalidated')
def step_impl(step):
    global g_addresses
    global g_events
    for event, address in zip(g_events, g_addresses):
        address_form = AddressForm(event)
        event_form = EventForm(address)
        assert address_form.is_valid() is False or event_form.is_valid() is False

use_step_matcher("parse")
@then(u'an error message "{error}" should be printed')
def print_error(step, error):
    global g_addresses
    global g_events
    for event, address in zip(g_events, g_addresses):
        address_form = AddressForm(event)
        event_form = EventForm(address)
        assert error in str(address_form.errors) or error in str(event_form.errors)

def create_events(context, min_cap):
    events = []
    addresses = []
    for row in context.table:
        event = {}
        event['name'] = row['evt_name']
        event['datetime'] = row['evt_date']
        event['fee'] = row['fee']
        event['max_capacity'] = row['max_cap']
        if min_cap: # Normal flow
            event['min_capacity'] = row['min_cap']
        #Alternate flow is min_cap not specified
        event['description'] = row['evt_details']
        event['category'] = row['category']
        address = {}
        address['city'] = row['city']
        address['street'] = row['street']
        address['number'] = row['number']
        address['postalcode'] = row['postalcode']
        events.append(event)
        addresses.append(address)
    return events, addresses
    

def save_events(events, addresses):
    for event, address in zip(events, addresses):
        address_form = AddressForm(address)
        assert address_form.is_valid() == True
        test_address = address_form.save()

        event_form = EventForm(event)
        assert event_form.is_valid()
        test_event = event_form.save(commit=False)
        test_event.address = test_address
        test_event.save()
