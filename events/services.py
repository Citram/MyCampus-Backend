from .models import *
import datetime

def create_event(name, datetime, fee, min_capacity, max_capacity, description, category):
    pass

def get_events_by_category(category):
    pass

def get_events_by_keywords(keywords):
    pass

def get_event_by_id(id):
    pass

def get_events_by_words_in_name(words):
    pass

def delete_event(event):
    pass

def create_comment(event, user, message):
    pass

def set_comment(event, user, massage):
    pass

def delete_comment(comment_id):
    pass

#================= Validators =================#
def validate_create_event(user, name, datetime, fee, min_capacity, max_capacity):
    pass

def validate_delete_comment(comment, user, ):
    pass

def validate_delete_event(event, user):
    pass

def validate_event_organizer(user, event):
    pass

#================= Helper functions =================#
def parse_datetime(time_string):
    """
    Parses the datetime string, from the ***toUTCString()*** method using javascript, into a datetime object
    Example, takes "Tue, 22 Nov 2011 06:00:00 GMT" into the corresponding object
    See this for details: https://stackoverflow.com/questions/8153631/js-date-object-to-python-datetime
    """
    datetimeobj = datetime.datetime.strptime(time_string, "%a, %d %b %Y %H:%M:%S %Z")
    return datetimeobj
