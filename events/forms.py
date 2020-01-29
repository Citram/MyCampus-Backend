import re
from django import forms
from django.core.validators import EmailValidator

class EventForm(forms.Form):
    #event name
    name = forms.CharField(label='Name', validators=[validate_event_name])
    
    #email and validations
    email_domains = [
        'mail.mcgill.ca'
        'mcgill.ca'
    ]
    email_validator = EmailValidator(message='Please enter a valid McGill email address',
                                     whitelist=email_domains)
    email = forms.EmailField(null=False, blank=False, unique=True, validators=[email_validator])

    #event datetime
    datetime = forms.DateTimeField(label='Event start time', validators=[validate_event_datetime])

    #participation fee
    fee = forms.DecimalField(label='Event start time', min_value=0, max_digits=5, decimal_places=2)

    #capacities
    #TODO: find to way to properly validate the numbers
    max_capacity = forms.IntegerField(label='Maximum capacity for the event', min_value=1)
    min_capacity = forms.IntegerField(label='Minimum number of people required')

    #event category
    #TODO
    EVENT_OUTDOOR = 'OUT'
    EVENT_GAMING = 'GAM'

    CATEGORIES = [
        (EVENT_OUTDOOR, 'Outdoor events'),
        (EVENT_GAMING, 'Games')
    ]
    category = forms.ChoiceField(label='Event category', choices=CATEGORIES, validators=[validate_event_category])

class CommentForm(forms.Form):

    #massage
    message = forms.Textarea('Your message: ')

#==================== event validators ====================#
def validate_event_name(name):
    pattern = re.compile('[a-zA-Z]+')
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
