
import re
from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Admin, Organization, Student, Review, UserFlag
from django.utils.translation import gettext_lazy as _ #not sure if this is needed but apparently its good?


#=========================== User forms ===========================#
class AdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = [
            'id',
            'password',
            'email'
        ]
        labels = {
            'id': _('Username'),
            'password': _('Password'),
            'email': _('Email Address')
        }

    def clean_email(self):
        email_input = self.cleaned_data['email']
        if '@mcgill.ca'in email_input or '@mail.mcgill.ca' in email_input:
            return email_input
        else:
            raise forms.ValidationError(_('Please enter a valid McGill email address'))

    def clean_id(self):
        id_input = self.cleaned_data['id']
        pattern = re.compile('^[a-zA-Z0-9]{5,20}$')
        if not (pattern.match(id_input)):
            raise forms.ValidationError(_(
                'Your username must be between 5 and 20 characters long and only contain letters, numbers and the period'))
        else:
            return id_input

    def clean_password(self):
        password_input = self.cleaned_data['password']
        pattern = re.compile("^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,}$")
        if not (pattern.match(password_input)):
            raise forms.ValidationError(_(
                'Your password must be at least 8 characters long and contain at least a letter, a number and a special character.'))
        else:
            return password_input
        

class OrganizationForm(AdminForm):

      
    class Meta:
        model = Organization
        fields = [
            'id',
            'password',
            'email',
            'name',
            'description'
        ]
        labels = {
            'id': _('Username'),
            'password': _('Password'),
            'email': _('Email Address'),
            'name': _('Name'),
            'description': _('Description')
        }

    def clean_name(self):
        name_input = self.cleaned_data['name']
        pattern  = re.compile("^[A-Za-z]+((\\s)?((\\'|\\-|\\.)?([A-Za-z])+))*$")
        if not (pattern.match(name_input)):
            raise forms.ValidationError(_(
                'Please enter a valid name.'))
        else:
            return name_input
        

    def clean_description(self):
        description_input = self.cleaned_data['description']
        if description_input is None or description_input.strip() == '':
            raise forms.ValidationError(_('You cannot enter an empty description.'))
        else:
            return description_input

class StudentForm(OrganizationForm):


    faculty = forms.ChoiceField(
        choices=Student.FACULTIES,
        required=False
    )

    
    gender = forms.ChoiceField(
        choices=Student.GENDERS,
        required=False
    )

    class Meta:
        model = Student
        fields = [
            'id',
            'password',
            'email',
            'name',
            'description',
            'age',
            'gender',
            'faculty'
        ]
        labels = {
             'id': _('Username'),
             'password': _('Password'),
             'email': _('Email Address'),
             'name': _('Name'),
             'description': _('Description'),
             'age': _('Age'),
             'gender': _('Gender'),
             'faculty': _('Faculty')
        }
        widgets = {
            'password' : forms.PasswordInput()
        }

    def clean_age(self):
        age_input = self.cleaned_data['age']
        if not (age_input > 16 or age_input < 100):
            raise forms.ValidationError(_('Please enter a valid age.'))
        else:
            return age_input

    def clean_gender(self):
        sex_input = self.cleaned_data['gender']
        if sex_input is None or (sex_input != 'M' and sex_input != 'F'):
            raise forms.ValidationError(_('Please enter a valid gender.'))
        else:
            return sex_input

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)