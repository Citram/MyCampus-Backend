<<<<<<< HEAD
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

    def clean_date(self):
        date_input = self.cleaned_data['date']
        if date_input.date < datetime.date.today:
            raise forms.ValidationError('You cannot enter an event date that is before today.')

    def clean_fee(self):
        fee_input = self.cleaned_data['fee']
        if fee_input < 0 or fee_input > 500:
            raise forms.ValidationError('You cannot enter a fee that is negative and you cannot try to scam people.')

    def clean_max_capacity(self):
        max_capacity_input = self.cleaned_data['max_capacity']
        if max_capacity_input < 1 or max_capacity_input > 9000:
            raise forms.ValidationError('You cannot enter a maximum capacity less than 1 or more than 9000.')

    def clean_min_capacity(self):
        min_capacity_input = self.cleaned_data['min_capacity']
        if min_capacity_input < 1 or min_capacity_input > 9000:
            raise forms.ValidationError('You cannot enter a minimum capacity less than 1 or more than 9000.')
    
    def clean_description(self):
        description_input = self.cleaned_data['description']
        if description_input is None or description_input.strip() == '':
            raise forms.ValidationError('You cannot enter an empty description.')

    def clean_category(self):
        category_input = self.cleaned_data['category']
        for option in Event.CATEGORIES:
            if category_input == option[0]:
                return
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

class DeleteEventForm(Form):
    id_field = CharField()


