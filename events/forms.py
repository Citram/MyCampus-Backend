import re
import datetime
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

    def clean_name(self):
        name_input = self.cleaned_data['name']
        if name_input is None or name_input.strip() == '':
            raise forms.ValidationError('You cannot enter an empty name.')
        else:
            return name_input

    def clean_date(self):
        date_input = self.cleaned_data['date']
        if date_input.date < datetime.date.today:
            raise forms.ValidationError('You cannot enter an event date that is before today.')
        else:
            return date_input

    def clean_fee(self):
        fee_input = self.cleaned_data['fee']
        if fee_input < 0 or fee_input > 500:
            raise forms.ValidationError('You cannot enter a fee that is negative and you cannot try to scam people.')
        else:
            return fee_input

    def clean_max_capacity(self):
        max_capacity_input = self.cleaned_data['max_capacity']
        if max_capacity_input < 1 or max_capacity_input > 9000:
            raise forms.ValidationError('You cannot enter a maximum capacity less than 1 or more than 9000.')
        else:
            return max_capacity_input

    def clean_min_capacity(self):
        min_capacity_input = self.cleaned_data['min_capacity']
        if min_capacity_input < 1 or min_capacity_input > 9000:
            raise forms.ValidationError('You cannot enter a minimum capacity less than 1 or more than 9000.')
        elif min_capacity_input > self.cleaned_data['max_capacity']:
            raise forms.ValidationError('You cannot enter a minimum capacity higher than your maximum capacity.')
        else:
            return min_capacity_input
            
    
    def clean_description(self):
        description_input = self.cleaned_data['description']
        if description_input is None or description_input.strip() == '':
            raise forms.ValidationError('You cannot enter an empty description.')
        else:
            return description_input

    def clean_category(self):
        category_input = self.cleaned_data['category']
        for option in Event.CATEGORIES:
            if category_input == option[0]:
                return category_input
        raise forms.ValidationError('You cannot enter an invalid event category.')


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

    #pass in hidden field for event id from view???

    def clean_message(self):
        message_input = self.cleaned_data['message']
        if message_input is None or message_input.strip()=='':
            raise forms.ValidationError('You cannot enter an empty message.')

class DeleteEventForm(forms.Form):
    id_field = forms.CharField()

class RegistrationForm(forms.Form):
    event_id = forms.CharField(widget=forms.HiddenInput())
    





