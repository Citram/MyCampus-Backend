from .models import *
from users.models import *
from django.contrib.auth.models import User

import datetime
from django.http import JsonResponse
from django.db.models import Q

#====== Exception class ======#
class UnsuccessfulOperationError(Exception):
    def __init__(self, message, error_source):
        super(UnsuccessfulOperationError, self).__init__(message)
        self.error_source = error_source

#================= Helper functions =================#
def parse_datetime(time_string):
    """
    Parses the datetime string, from the ***toUTCString()*** method using javascript, into a datetime object
    Example, takes "Tue, 22 Nov 2011 06:00:00 GMT" into the corresponding object
    See this for details: https://stackoverflow.com/questions/8153631/js-date-object-to-python-datetime
    """
    datetimeobj = datetime.datetime.strptime(time_string, "%a, %d %b %Y %H:%M:%S %Z")
    return datetimeobj

def events_to_json(events):
    """
    renders a list of events to a dictionary to be passed into a JsonResponse
    dictionary (list of events) contains a list of dictionaries (events)
    each event contains id, name, date, fee, capacities
    """
    result = {}
    index = 0
    for e in events:
        event = {}
        event['id'] = e.id
        event['name'] = e.name
        event['datetime'] = e.datetime
        event['fee'] = e.fee
        event['max_capacity'] = e.max_capacity
        event['min_capacity'] = e.min_capacity
        result['event'+str(index)] = event
        index += 1
    return result

#================= Services =================#

def create_event(name_input, datetime_input, fee_input, min_capacity_input, max_capacity_input, description_input, category_input):
    event = Event(
        name=name_input,date=parse_datetime(datetime_input),
        fee=fee_input,min_capacity=min_capacity_input, 
        max_capacity=max_capacity_input, description=description_input,
        category=category_input
    )
    event.save()


def get_events_by_category(category_input):
    events = Event.objects.filter(category=category_input)
    if len(events) == 0:
        raise UnsuccessfulOperationError('No events in this category has been found', 'no events found')
    else:
        result = JsonResponse(events_to_json(events))
        return result

def get_events_by_keywords(keywords):
    # TODO instead of AND, how to we do OR???
    # check this out but IDK how to deal with a for loop
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#complex-lookups-with-q
    events = Event.objects.all()
    for kw in keywords:
        events = events.filter(description__icontains=kw)
    if len(events) == 0:
        raise UnsuccessfulOperationError('No events with such description has been found', 'no events found')
    else:
        result = JsonResponse(events_to_json(events))
        return result

def get_events_by_words_in_name(words):
    events = Event.objects.all()
    for kw in words:
        events = events.filter(name__icontains=kw)
    if len(events) == 0:
        raise UnsuccessfulOperationError('No events wiuth such name has been found', 'no events found')
    else:
        result = JsonResponse(events_to_json(events))
        return result

def get_event_by_name_test(event_name):
    try:
        return Event.objects.get(name=event_name)
    except:
        raise UnsuccessfulOperationError('Event not found with name ', 'event_name')


def delete_event_by_name(event_name):
    try:
        Event.objects.get(name=event_name).delete()
    except:
        raise UnsuccessfulOperationError('Event not found with name ', 'event_name')

def delete_event(event_id):
    try:
        Event.objects.get(id=event_id).delete()
    except:
        raise UnsuccessfulOperationError('Event not found with id ', 'event_id')

def get_event_by_id(id):
    try:
        event = Event.objects.get(pk=id)
        return event
    except:
        raise UnsuccessfulOperationError('Invalid event id', 'event_id')

def create_comment(event_id, user_id, message_input):
    try:
        event = Event.objects.get(id=event_id)
    except:
        raise UnsuccessfulOperationError('Event not found with id', 'event_id')
    try:
        user = RegularUser.objects.get(user_id)
    except:
        raise UnsuccessfulOperationError('User not found with id', 'user_id')

    comment = Comment(message=message_input)
    comment.author = user
    comment.event = event
    comment.save()

def set_comment(comment_id, massage_input):
    try:
        comment = Comment.objects.get(id=comment_id)
    except:
        raise UnsuccessfulOperationError('Comment not found with id', 'comment_id')
    comment.message = massage_input
    comment.save()

def delete_comment(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except:
        raise UnsuccessfulOperationError('Comment not found with id', 'comment_id')
    comment.delete()

def join_event (user_id, event_id, date=datetime.date.today()):
    try:
        event = Event.objects.get(id=event_id)
    except:
        raise Exception('Event not found with id', 'event_id')
    try:
        user = User.objects.get(id=user_id)
    except:
        raise Exception('User not found with id', 'user_id')

    if date > event.datetime:
        raise Exception("Event has already occurred.")

    if event.attendees.count() >= event.max_capacity:
        raise Exception("Max capacity of event reached.")


    event.attendees.add(user)
    event.save()
    return True

def leave_event(user_id, event_id, date=datetime.date.today()):
    try:
        event = Event.objects.get(id=event_id)
    except:
        raise UnsuccessfulOperationError('Event not found with id', 'event_id')
    try:
        user = User.objects.get(id=user_id)
    except:
        raise UnsuccessfulOperationError('User not found with id', 'user_id')
  
    if date > event.datetime:
        raise UnsuccessfulOperationError("Event has already occurred.", 'event_id')

    if not user in event.attendees.all():
        raise UnsuccessfulOperationError('User is not signed up for event.', 'user_id')
    else:
        event.attendees.remove(user)
    return True