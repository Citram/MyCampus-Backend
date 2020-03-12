from django.test import TestCase
from django.test import Client
from .services import *
from .forms import EventForm, AddressForm, DeleteEventForm
from .models import Event, Address, Comment
from .views import *
from users.models import *
from events.services import UnsuccessfulOperationError
from hashid_field import Hashid
from users.models import *
from users.forms import *
from hashid_field import Hashid
from users.models import *
from users.forms import *


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

class EventFormTest(TestCase):
    
    # Arbitrary data for event form and address form
    # Not sure how to enter the date string with hours
    data_event = {
        'name': 'Dungeon & Dragons',
        'fee': 69,
        'max_capacity': 420,
        'min_capacity': 69,
        'datetime': "2022-02-02",
        'description': 'Random event',
        'category': 'GAM'
    }

    data_address = {
        'city': 'Montreal',
        'street': 'Sherbrooke Av.',
        'number': '1980',
        'postalcode': 'H6J3T5'
    }
# TEST CREATE EVENT COMMENTED : IS MAKING AN ERROR ON TESTING

#    Address object must exist in the database first to not violate any foreign key constraint in the Event model
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
        self.assertEqual(event.datetime.strftime("%Y-%m-%d"), EventFormTest.data_event.get('datetime'))
        self.assertEqual(event.fee, EventFormTest.data_event.get('fee'))
        self.assertEqual(event.max_capacity, EventFormTest.data_event.get('max_capacity'))
        self.assertEqual(event.min_capacity, EventFormTest.data_event.get('min_capacity'))
        self.assertEqual(event.description, EventFormTest.data_event.get('description'))
        self.assertEqual(event.category, EventFormTest.data_event.get('category'))
        self.assertEqual(event.address.city, EventFormTest.data_address.get('city'))
        self.assertEqual(event.address.street, EventFormTest.data_address.get('street'))
        self.assertEqual(event.address.number, EventFormTest.data_address.get('number'))
        self.assertEqual(event.address.postalcode, EventFormTest.data_address.get('postalcode'))

    def test_create_event_empty_name(self):
            event_form = EventForm({
                'name': '',
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_empty_date(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': '',
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())
    def test_create_event_invalid_date(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': '2019-01-01',
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_empty_fee(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': None,
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_invalid_fee(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': -1,
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': 10000000,
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_empty_max_capacity(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': None,
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_invalid_max_capacity(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': -1,
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': 32894798,
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_invalid_min_capacity(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': -1,
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': 234857893452347,
                'description': EventFormTest.data_event.get('description'),
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())
    def test_create_event_empty_description(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': '',
                'category': EventFormTest.data_event.get('category')
            })

            self.assertFalse(event_form.is_valid())

    def test_create_event_empty_category(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': ''
            })
            self.assertFalse(event_form.is_valid())

    def test_create_event_invalid_category(self):
            event_form = EventForm({
                'name': EventFormTest.data_event.get('name'),
                'datetime': EventFormTest.data_event.get('datetime'),
                'fee': EventFormTest.data_event.get('fee'),
                'max_capacity': EventFormTest.data_event.get('max_capacity'),
                'min_capacity': EventFormTest.data_event.get('min_capacity'),
                'description': EventFormTest.data_event.get('description'),
                'category': 'NON'
            })

            self.assertFalse(event_form.is_valid())

class EventDeleteFormTest(TestCase):
    def setUp(self):
        Event.objects.create(name="Event1",date="2022-02-02",fee=70,min_capacity=0, max_capacity=80, description="description",
        category='GAM')

    def delete_event_by_id(self):
        event=Event.objects.get(name="Event1")
        services.delete_event(event_id=event.id)
        self.assertTrue(Event.objects.all().count(), 0)
    
    def delete_event_invalid_id(self):
        try:
            services.delete_event("FalseID")
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "Event not found with id")

    def delete_event_by_name(self):
        event=Event.objects.get(name="Event1")
        services.delete_event_by_name(event.name)
        
        self.assertTrue(Event.objects.all().count(), 0)
    
    def delete_event_invalid_name(self):
        try:
            services.delete_event("FalseName")
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "Event not found with id")


class LeaveEventTestCase(TestCase):
    def setUp(self):
        #second implement

        Event.objects.create(name="Event1",date="2022-02-02",fee=70,min_capacity=0, max_capacity=80, description="description",
        category='GAM')

        Student.objects.create(name="TestStudent", description="This guy just leaves events",
        age=20, rating=4)

    #TODO make sure this actually makes sense
    def leave_event(self):
        student=Student.objects.get(name="TestStudent")
        event=Event.objects.get(name="Event1")
        event.attendees.add(student)
        event.save()
        services.leave_event(user_id=student.id, event_id=event.id)
        self.assertNotIn(student,event.attendees)
    
    def leave_event_invalid_event(self):
        student=Student.objects.get(name="TestStudent")
        try:
            services.leave_event(user_id=student.id, event_id="Event2")
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "Event not found with id")

    def leave_event_invalid_user(self):
        event=Event.objects.get(name="Event1")
        try:
            services.leave_event(user_id="112", event_id=event.id)
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "User not found with id")

    def leave_event_no_relation(self):
        student=Student.objects.get(name="TestStudent")
        event=Event.objects.get(name="Event1")
        try:
            services.leave_event(user_id=student.id, event_id=event.id)
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "User not attending event")

#TODO actually implement this because right now it does not make sense
'''
class LeaveEventViewTest(TestCase):
    c = Client()
    def test_response_please(self):
       c = Client()
       response = c.post('/event/leave')
       self.assertEqual(200, response.status_code)

'''

class JoinEventTestCase(TestCase):
    def setUp(self):

        Event.objects.create(name="Event1",date="2022-02-02",fee=70,min_capacity=0, max_capacity=80, description="description",
        category='GAM')

        Student.objects.create(name="TestStudent", description="This guy just leaves events",
        age=20, rating=4)
    def join_event(self):

        student=Student.objects.get(name="TestStudent")
        event=Event.objects.get(name="Event1")
        services.join_event(user_id=student.id, event_id=event.id)
        self.assertIn(student,event.attendees)
        self.assertIn(event, student.events)

    def join_event_invalid_user_id(self):
        event=Event.object.get(name="Event1")
        try:
            services.leave_event(user_id="FalseStudent", event_id=event.id)
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "User not found with id")
        
    def join_event_invalid_event_id(self):
        student=Student.objects.get(name="TestStudent")
        try:
            services.leave_event(user_id=student.id, event_id="FalseEvent")
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, "User not found with id")
    
class JoinDeletedEventTestCase(TestCase):
    def setUp(self):

        Event.objects.create(name="Event1",date="2022-02-02",fee=70,min_capacity=0, max_capacity=80, description="description",
        category='GAM')

        Student.objects.create(name="TestStudent", description="This guy just leaves events",
        age=20, rating=4)

    def join_deleted_event(self):
        event = Event.objects.get(name="Event1")
        student = Student.objects.get(name="TestStudent")

        event_Id = event.id
        
        services.delete_event(event_id=event_Id)
        self.assertTrue(Event.objects.all().count(), 0)
        try:
            services.join_event(student_id=student.id, event_id=event_Id)
        except UnsuccessfulOperationError as e:
            self.assertEqual(e, 'Event not found with id')

#class EditDeletedEventTestCase(TestCase):
    
# Test suite for Event views
#TODO completely fix because this is sketch

class EventViewTest(TestCase):
    c = Client()

class CreateEventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="Event1",date="2022-02-02",fee=70,min_capacity=0, max_capacity=80, description="description", category='GAM')
        Student.objects.create(name="TestStudent", description="This guy just leaves events",
            age=20, rating=4)

    def create_event(self):
        student = Student.objects.get(name="TestStudent")
        event=Event.objects.get(name="Event1")
        name_Input=student.name
        datetime_Input=event.datetime
        fee_Input=event.fee
        min_capacity_Input=event.min_capacity
        max_capacity_Input=event.max_capacity
        description_Input=event.description
        category_Input=event.category
        services.create_event(name_input=name_Input,datetime_input=datetime_Input,fee_input=fee_Input,
            min_capacity_input=min_capacity_Input,max_capacity_input=max_capacity_Input,
            description_input=description_Input,category_input=category_Input)
        self.assertIn(event,Event.objects.all())

# Test suite for Event services
class EventServiceTest(TestCase):


    data_event = {
        'name': 'Dungeon & Dragons',
        'fee': 69,
        'max_capacity': 420,
        'min_capacity': 69,
        'datetime': "2022-02-02",
        'description': 'Random event',
        'category': 'GAM'
    }

    data_address = {
        'city': 'Montreal',
        'street': 'Sherbrooke Av.',
        'number': '1980',
        'postalcode': 'H6J3T5'
    }

    data_user = {
        'id': 'achoi26',
        'password': 'lL09dshgfsy&',
        'email': 'pp69@mail.mcgill.ca',
        'name': 'Alex Choi',
        'description': 'pp69',
        'age': 69,
        'gender': 'M',
        'faculty': 'Eng'
    }

    def test_response_please(self):
       c = Client()
    #    response = HttpResponse()
       response = c.post('/login/')
       self.assertEqual(200, response.status_code)

    def test_delete_event(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()
        events = Event.objects.all() # Get all objects from database
        self.assertTrue(len(events), 1)
        delete_event(events[0].id)
        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 0)

    def test_delete_event_fail_invalid_id(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()
        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 1)
        with self.assertRaises(Exception): delete_event('Invalid Name')

    def test_delete_event_fail_empty_id(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()
        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 1)
        with self.assertRaises(Exception): delete_event('')
    
    def test_get_event_by_id(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()

        event_id = test_event.id

        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 1)
        event_id = events[0].id
        retrieved_event = get_event_by_id(event_id)

        self.assertEqual(retrieved_event.name, EventFormTest.data_event.get('name'))
        self.assertEqual(retrieved_event.datetime.strftime("%Y-%m-%d"), EventFormTest.data_event.get('datetime'))
        self.assertEqual(retrieved_event.fee, EventFormTest.data_event.get('fee'))
        self.assertEqual(retrieved_event.max_capacity, EventFormTest.data_event.get('max_capacity'))
        self.assertEqual(retrieved_event.min_capacity, EventFormTest.data_event.get('min_capacity'))
        self.assertEqual(retrieved_event.description, EventFormTest.data_event.get('description'))
        self.assertEqual(retrieved_event.category, EventFormTest.data_event.get('category'))
        self.assertEqual(retrieved_event.address.city, EventFormTest.data_address.get('city'))
        self.assertEqual(retrieved_event.address.street, EventFormTest.data_address.get('street'))
        self.assertEqual(retrieved_event.address.number, EventFormTest.data_address.get('number'))
        self.assertEqual(retrieved_event.address.postalcode, EventFormTest.data_address.get('postalcode'))

    def test_get_event_by_id_fail_invalid_id(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()

        event_id = test_event.id

        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 1)
        event_id = events[0].id
        with self.assertRaises(Exception): get_event_by_id(1234)
    
    def test_get_event_by_id_fail_empty_id(self):
        address_form = AddressForm(EventServiceTest.data_address)
        self.assertTrue(address_form.is_valid())
        test_address = address_form.save()

        event_form = EventForm(EventServiceTest.data_event)
        self.assertTrue(event_form.is_valid())

        test_event = event_form.save(commit=False)
        test_event.address = test_address # Insert the Address association
        test_event.save()

        event_id = test_event.id

        events = Event.objects.all() # Get all objects from database
        self.assertEqual(len(events), 1)
        event_id = events[0].id
        with self.assertRaises(Exception): get_event_by_id()