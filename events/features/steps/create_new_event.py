from behave import *
from events.forms import EventForm, AddressForm
from events.models import Event, Address

@given(u'Student "{name}" is logged in')
def student_logged_in(step, name):
    pass

@when(u'the student requests to create an event')
def step_impl(context):
    for row in context.table:
        event = {}
        event['name'] = row['evt_name']
        event['datetime'] = row['evt_date']
        event['fee'] = row['fee']
        event['max_capacity'] = row['max_cap']
        event['min_capacity'] = 1
        event['description'] = row['evt_details']
        event['category'] = row['category']
        address = {}
        address['city'] = row['city']
        address['street'] = row['street']
        address['number'] = row['number']
        address['postalcode'] = row['postalcode']

        address_form = AddressForm(address)
        assert address_form.is_valid() == True
        test_address = address_form.save()

        event_form = EventForm(event)
        assert event_form.is_valid()
        test_event = event_form.save(commit=False)
        test_event.address = test_address
        test_event.save()

@then(u'the event should with name <evt_name> should be created and stored in the system')
def step_impl(context):
    events = Event.objects.all()
    for idx, row in enumerate(context.table):
        event = events[idx]
        assert event.name == row['evt_name']
        assert event.datetime.strftime("%Y-%m-%d") == row['evt_date']
        assert int(event.fee) == int(row['fee'])
        assert int(event.max_capacity) == int(row['max_cap'])
        assert event.description == row['evt_details']
        assert event.category == row['category']
        
        address = event.address
        assert address.city == row['city']
        assert address.street == row['street']
        assert address.number == row['number']
        assert address.postalcode == row['postalcode']
        
        
        
