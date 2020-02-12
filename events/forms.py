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

    def clean_name(self):
        #TODO
        return

    def clean_date(self):
        #TODO

    def clean_fee(self):
        #TODO

    def clean_max_capacity(self):
        #TODO

    def clean_min_capacity(self):
        #TODO
    
    def clean_description(self):
        #TODO

    def clean_category(self):
        #TODO

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

