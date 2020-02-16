from django.test import TestCase
from django.test import Client
from .forms import EventForm, AddressForm, DeleteEventForm
from .models import Event, Address, Comment
from .views import *

# Address form test sutie
class AddressFormTest(TestCase):
    data_address = {
        'city': 'Montreal',
        'street': 'Sherbrooke Av.',
        'number': '1980',
        'postalcode': 'H6J3T5'
    }

def test_create_address_form(self):
        address_form = AddressForm(AddressFormTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()
        addresses = Address.objects.all()
        address = addresses[0]
        self.assertEqual(1, len(addresses))
        self.assertEqual(address.city, AddressFormTest.data_address.get('city'))
        self.assertEqual(address.street, AddressFormTest.data_address.get('street'))
        self.assertEqual(address.number, AddressFormTest.data_address.get('number'))
        self.assertEqual(address.postalcode, AddressFormTest.data_address.get('postalcode'))

def test_create_address_form_empty_city(self):
        address_form = AddressForm({
            'city': '',
            'street': AddressFormTest.data_address.get('street'),
            'number': AddressFormTest.data_address.get('number'),
            'postalcode': AddressFormTest.data_address.get('postalcode')
        })

        self.assertFalse(address_form.is_valid())

def test_create_address_form_empty_street(self):
        address_form = AddressForm({
            'city': AddressFormTest.data_address.get('city'),
            'street': '',
            'number': AddressFormTest.data_address.get('number'),
            'postalcode': AddressFormTest.data_address.get('postalcode')
        })

        self.assertFalse(address_form.is_valid())

def test_create_address_form_empty_number(self):
        address_form = AddressForm({
            'city': AddressFormTest.data_address.get('city'),
            'street': AddressFormTest.data_address.get('street'),
            'number': '',
            'postalcode': AddressFormTest.data_address.get('postalcode')
        })

        self.assertFalse(address_form.is_valid())

def test_create_address_form_empty_postalcode(self):
        address_form = AddressForm({
            'city': AddressFormTest.data_address.get('city'),
            'street': AddressFormTest.data_address.get('street'),
            'number': AddressFormTest.data_address.get('number'),
            'postalcode': ''
        })

        self.assertFalse(address_form.is_valid())