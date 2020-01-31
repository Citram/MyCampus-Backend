
import re
from django import forms
from django.core.validators import EmailValidator


#=========================== User forms ===========================#
class UserForm(forms.Form):

    id = forms.CharField(label='Your username',
                         help_text='Your username may consist of upper and lower characters, numbers and periods',
                         max_length=20, validators=[username_validator])

    password = forms.CharField(label='password',max_length=64, widget=forms.PasswordInput) #password restrictions?

    #email and validations
    email_domains = [
        'mail.mcgill.ca'
        'mcgill.ca'
    ]
    class RangerRegistrationForm(forms.Form):
    email = forms.EmailField(label=_("Email Address"))

    def clean_email(self):
        submitted_data = self.cleaned_data['email']
        if '@gmail.com' not in submitted_data:
            raise forms.ValidationError('You must register using a Gmail address')
        return submitted_data


class AdminForm(UserForm):
    #subject ot change
    pass

class RegularUserForm(UserForm):

    name = forms.CharField(label='Your organization\'s name: ', max_length=30,
                           min_length=2, validators=[organization_name_validator])
    description = forms.CharField(label='A short discription about your organization', max_length=400)

class StudentForm(RegularUserForm):

    #override
    name = forms.CharField(label='Your name: ', max_length=30, min_length=2, validators=[student_name_validator])
    description = forms.CharField(label='A short discription about yourself', max_length=400)

    age = forms.IntegerField(label='Your age', min_value=12, max_value=120)

    #ThErE aRe OnLy TwO gEnDeRs
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    gender = forms.ChoiceField(choices=GENDERS, label='Your gender', required=False)

    #faculties
    FACULTY_AGRICULTURAL_AND_ENVIRONMENTAL_SCIENCES = 'AGR'
    FACULTY_ARTS = 'ART'
    FACULTY_CONTINUING_STUDIES = 'CNT'
    FACULTY_DENTISTRY = 'DNT'
    FACULTY_EDUCATION = 'EDU'
    FACULTY_ENGINEERING = 'ENG'
    FACULTY_GRADUATE_AND_POSTDOCTORAL_STUDIES = 'GRD'
    FACULTY_LAW = 'LAW'
    FACULTY_MANAGEMENT = 'MNG'
    FACULTY_MEDICINE = 'MED'
    FACULTY_MUSIC = 'MUS'
    FACULTY_SCIENCE = 'SCI'
    ALUMNI = 'ALU'

    FACULTIES = [
        (FACULTY_AGRICULTURAL_AND_ENVIRONMENTAL_SCIENCES, 'Faculty of Agricultural and Environmental Sciences'),
        (FACULTY_ARTS, 'Faculty of Arts'),
        (FACULTY_CONTINUING_STUDIES, 'School of Continuing Studies'),
        (FACULTY_DENTISTRY, 'Faculty of Dentistry'),
        (FACULTY_EDUCATION, 'Faculty of Education'),
        (FACULTY_ENGINEERING, 'Faculty of Engineering'),
        (FACULTY_GRADUATE_AND_POSTDOCTORAL_STUDIES, 'Graduate and Postdoctoral Studies'),
        (FACULTY_LAW, 'Faculty of Law'),
        (FACULTY_MANAGEMENT, 'Desautels Faculty of Management'),
        (FACULTY_MEDICINE, 'Faculty of Medicine'),
        (FACULTY_MUSIC, 'Schulich School of Music'),
        (FACULTY_SCIENCE, 'Faculty of Science'),
        (ALUMNI, 'Alumni'),
    ]

    faculty = forms.ChoiceField(choices=FACULTIES, label='Your faculty', required=False)

class OrganizationForm(RegularUserForm):
    pass

#=========================== Comment form ===========================#


#=========================== Flag form ===========================#


#================ validators ================#
def username_validator(username):
    pattern = re.compile("^[A-Za-z\\d.]*$") #upper,lower, digits and '.' only
    return pattern.match(username)

def organization_name_validator(name):
    pattern = re.compile("") #TODO
    return pattern.match(name)

def student_name_validator(name):
    pattern = re.compile("") #TODO
    return pattern.match(name)