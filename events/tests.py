from django.test import TestCase
from .forms import EventForm, AddressForm, DeleteEventForm
from .models import Event, Address, Comment
import datetime

# Event Test Suite
class EventFormTest(TestCase):
    
    #Arbitrary data for event form and address form
    data_event = {
        'name': 'Dungeon & Dragons',
        'date': '2021-01-01',
        'fee': 69,
        'max_capacity': 420,
        'min_capacity': 69,
        'description': 'Random event',
        'category': 'GAM'
    }

    data_address = {
        'city': 'Montreal',
        'street': 'Sherbrooke Av.',
        'number': '1980',
        'postalcode': 'H6J3T5'
    }
    
    # Address object must exist in the database first to not violate any foreign key constraint in the Event model
    def test_create_address(self):
        address_form = AddressForm(EventFormTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()
        addresses = Address.objects.all()
        address = addresses[0]
        self.assertEqual(1, len(addresses))
        self.assertEqual(address.city, EventFormTest.data_address.get('city'))
        self.assertEqual(address.street, EventFormTest.data_address.get('street'))
        self.assertEqual(address.number, EventFormTest.data_address.get('number'))
        self.assertEqual(address.postalcode, EventFormTest.data_address.get('postalcode'))

    def test_create_event(self):
        address_form = AddressForm(EventFormTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventFormTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()
        events = Event.objects.all() # Get all objects from database
        event = events[0]

        self.assertEqual(1, len(events))
        self.assertEqual(event.name, EventFormTest.data_event.get('name'))
        self.assertEqual(event.date.strftime("%Y-%m-%d"), EventFormTest.data_event.get('date'))
        self.assertEqual(event.fee, EventFormTest.data_event.get('fee'))
        self.assertEqual(event.max_capacity, EventFormTest.data_event.get('max_capacity'))
        self.assertEqual(event.min_capacity, EventFormTest.data_event.get('min_capacity'))
        self.assertEqual(event.description, EventFormTest.data_event.get('description'))
        self.assertEqual(event.category, EventFormTest.data_event.get('category'))
        self.assertEqual(event.address.city, EventFormTest.data_address.get('city'))
        self.assertEqual(event.address.street, EventFormTest.data_address.get('street'))
        self.assertEqual(event.address.number, EventFormTest.data_address.get('number'))
        self.assertEqual(event.address.postalcode, EventFormTest.data_address.get('postalcode'))