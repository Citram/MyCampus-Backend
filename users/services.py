from .models import *
from users.models import *
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

#================= Services =================#

#Create the user
def create_user( id_user, password, email):
    user = User(
        id=id_user,password=password,
        email=email
    )
    user.save()

#Get the user
def get_user():
    return user = User.objects.all()

