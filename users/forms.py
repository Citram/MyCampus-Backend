import re
from django import forms
from django.core.validators import EmailValidator
from .models import Admin, Organization, Student, Review, UserFlag


#=========================== User forms ===========================#
class AdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = [
            'id',
            'password',
            'email'
        ]

    def clean_email(self):
        email_input = self.cleaned_data['email']
        if '@mcgill.ca'in email_input or '@mail.mcgill.ca' in email_input:
            return email_input
        else:
            raise forms.ValidationError('Please enter a valid McGill email address')

    def clean_id(self):
        id_input = self.cleaned_data['id']
        pattern = re.compile('^[\\p{L}\\p{Nd}.]{5,20}$')
        if not (pattern.match(id_input)):
            raise forms.ValidationError(
                'Your username must be between 5 and 20 characters long and only contain letters, numbers and the period')
        else:
            return id_input

    def clean_password(self):
        password_input = self.cleaned_data['password']
        pattern = re.compile("^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,}$")
        if not (pattern.match(password_input)):
            raise forms.ValidationError(
                'Your password must be at least 8 characters long and contain at least a letter, a number and a special character.')
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

    def clean_name(self):
        name_input = self.cleaned_data['name']
        pattern  = re.compile("^[A-Za-z]+((\\s)?((\\'|\\-|\\.)?([A-Za-z])+))*$")
        if not (pattern.match(name_input)):
            raise forms.ValidationError(
                'Please enter a valid name.')
        else:
            return name_input
        

    def clean_description(self):
        description_input = self.cleaned_data['description']
        if description_input is None or description_input.strip() == '':
            raise forms.ValidationError('You cannot enter an empty description.')
        else:
            return description_input

class StudentForm(OrganizationForm):

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
        widgets = {
            'password' : forms.PasswordInput()
        }

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

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

    def clean_email(self):
        #TODO

    def clean_id(self):
        #TODO

    def clean_password(self):
        #TODO

    def clean_name(self):
        #TODO

    def clean_description(slef):
        #TODO

    def clean_age(self):
        #TODO

    def clean_gender(self):
        #TODO

    def clean_faculty(self):
        #TODO

#=========================== Review form ===========================#

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            'rating',
            'comment',
            'author',
            'event'
        ]

        widgets = {
            'author' : forms.HiddenInput(),
            'event' : forms.HiddenInput()
        }

    def clean_rating(self):
        #TODO

    def clean_comment(self):
        #TODO

    # def clean_author(self):
    #     #TODO

    # def clean_event(self):
    #     #TODO

#=========================== Flag form ===========================#

class UserFlagForm(forms.ModelForm):

    class Meta:
        model = UserFlag
        fields = [
            'flag_type',
            'details',
            'author',
            'recepient'
        ]

        widgets = {
            'author' : forms.HiddenInput(),
            'recepient' : forms.HiddenInput()
        }

    def clean_flag_type(self):
        #TODO

    def clean_details(self):
        #TODO

    # def clean_author(self):
    #     #TODO

    # def clean_recipient(self):
    # 
    

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