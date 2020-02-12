import re
from django import forms
from django.core.validators import EmailValidator


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
        #TODO

    def clean_id(self):
        #TODO

    def clean_password(self):
        #TODO

class OrganizationForm(forms.ModelForm):

      
   class Meta:
        model = Organization
        fields = [
            'id',
            'password',
            'email',
            'name',
            'description'
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

class StudentForm(forms.ModelForm):

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