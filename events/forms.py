from django.forms import ModelForm
from events.models import Event, Address
#from pygeocoder import Geocoder

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'datetime', 'fee', 'max_capacity', 'min_capacity', 'description', 'category']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['number', 'city', 'street', 'postalcode']
    
    def clean(self):
        string_address = self.cleaned_data['number'] + " " + self.cleaned_data['street'] + ", " + self.cleaned_data['city'] + " " + self.cleaned_data['postalcode']
        # g = Geocoder()

        # #if not g.geocode(string_address).valid_address:
        #     #raise forms.ValidationError("Address is not valid.")
        #     pass
        return self.cleaned_data