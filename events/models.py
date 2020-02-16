from django.db import models
from hashid_field import HashidAutoField
import datetime

# Create your models here.
class Address(models.Model):
    """
    address for an event, could be unnecessary
    """
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=6)

class Event(models.Model):
    """
    Event organized by a student or a student body
    """
    id = HashidAutoField(primary_key=True)

    name = models.CharField(max_length=100)

    date = models.DateTimeField(default=datetime.date.today())

    fee = models.DecimalField(default=0, decimal_places=3, max_digits = 1000)

    max_capacity = models.PositiveSmallIntegerField()
    min_capacity = models.PositiveSmallIntegerField(default=1)

    #TODO
    EVENT_OUTDOOR = 'OUT'
    EVENT_GAMING = 'GAM'

    CATEGORIES = [
        (EVENT_OUTDOOR, 'Outdoor events'),
        (EVENT_GAMING, 'Games')
    ]

    description = models.CharField(max_length=500)
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES
    )

    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    organizer = models.ForeignKey('users.RegularUser', on_delete=models.PROTECT)
    attendees = models.ManyToManyField('users.Student')

class Comment(models.Model):
    """
    a message left on the page of an event
    """
    id = HashidAutoField(primary_key=True)

    message = models.CharField(max_length=300)

    #date & time
    time = models.DateTimeField(auto_now=True)

    #many-to-one relations
    author = models.ForeignKey('users.RegularUser', on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

