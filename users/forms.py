import re
from django import forms
from django.core.validators import EmailValidator
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

    def clean_email(self):
        email_input = self.cleaned_data['email']
        if '@mcgill.ca'in email_input or '@mail.mcgill.ca' in email_input:
            return email_input
        else:
            raise forms.ValidationError(_('Please enter a valid McGill email address'))

    def clean_id(self):
        id_input = self.cleaned_data['id']
        pattern = re.compile('^[\\p{L}\\p{Nd}.]{5,20}$')
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
        widgets = {
            'password' : forms.PasswordInput()
        }

    def clean_age(self):
        age_input = self.cleaned_data['age']
        if not age_input > 16 or age_input < 100:
            raise forms.ValidationError(_('Please enter a valid age.'))
        else:
            return age_input

    def clean_gender(self):
        sex_input = self.cleaned_data['gender']
        if sex_input in None or sex_input != 'M' or sex_input != 'F':
            raise forms.ValidationError(_('Please enter a valid gender.'))
        else:
            return sex_input

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    pass

class ResetEmailForm(forms.Form):
    pass

class ResetStudentForm(forms.Form):
    pass

class ResetOrganizationForm(forms.Form):
    pass

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
        rating_input = self.cleaned_data['rating']
        if not isinstance(rating_input, int) or rating_input >= 1 or rating_input <= 5:
            raise forms.ValidationError(_('Please enter a valid rating.'))
        else:
            return rating_input
        

#=========================== Flag form ===========================#

class UserFlagForm(forms.ModelForm):

    flag_type = forms.ChoiceField(
        choices=UserFlag.TYPES
    )


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
            'recepient' : forms.HiddenInput(),
            'details' : forms.Textarea()
        }

    def clean_flag_type(self):
        pass
        #TODO

    def clean_details(self):
        pass
        #TODO

    # def clean_author(self):
    #     #TODO

    # def clean_recipient(self):
    # 
    