import re
from django import forms
from .models import Event, Address


class EventForm(forms.ModelForm):
    """
        not sure about this one, but for documentation on ModelForm, see
        https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/

    """
    class Meta:
        model = Event
        fields = [
            'name',
            'date',
            'fee',
            'max_capacity',
            'min_capacity',
            'description',
            'category'
        ]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'city',
            'street',
            'number',
            'postalcode'
        ]

class CommentForm(forms.Form):

    #massage
    message = forms.Textarea('Your message: ')

#==================== event validators ====================#
def validate_event_name(name):
    pattern = re.compile('[a-zA-Z]+') #must contain at least one character
    return pattern.match(name)

def validate_event_datetime(datetime):
    pass

def validate_event_capacities(min_cap, max_cap):
    pass

def validate_event_category(category):
    pass

def validate_event_description(description):
    return (description is not None and description.strip() != "")

#==================== comment validators ====================#
def validate_comment_datetime(datetime):
    pass

def validate_comment_message(message):
    return (message is not None and message.strip() != "")