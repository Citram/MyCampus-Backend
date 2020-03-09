from django.test import TestCase
from .forms import UserForm, RegularUserForm, StudentForm

class UserFormTest(TestCase):
    
    def test_valid_user(self):
        user_form = UserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com'
        })
        self.assertTrue(user_form.is_valid())

    def test_invalid_email(self):
        user_form = UserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@yahoo.com'
        })
        self.assertFalse(user_form.is_valid())

    def test_invalid_username(self):
        user_form = UserForm({
            'id': 'user&&S name',
            'password': 'testpassword1',
            'email': 'email@gmail.com'
        })
        self.assertFalse(user_form.is_valid())

    def test_long_username(self):
        user_form = UserForm({
            'id': 'this_is_a_very_long_username_that_is_tested',
            'password': 'testpassword1',
            'email': 'email@gmail.com'
        })
        self.assertFalse(user_form.is_valid())

    def test_long_password(self):
        user_form = UserForm({
            'id': 'testuser1',
            'password': 'very_extraordinarily_long_password_that_will_definitely_fail_the_specified_tests_and_should_not_result_in_saving_in_the_system',
            'email': 'email@gmail.com'
        })
        self.assertFalse(user_form.is_valid())

    def test_fields_missing(self):
        user_form = UserForm({
            'id': 'testuser1',
            'email': 'email@gmail.com'
        })
        self.assertFalse(user_form.is_valid())

class RegularUserFormTest(TestCase):
    
    def test_valid_regular_user(self):
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'validname',
            'description': 'valid_description'
        })
        self.assertTrue(user_form.is_valid())

    def test_invalid_name(self):
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'invali d&$_name',
            'description': 'valid_description'
        })
        self.assertFalse(user_form.is_valid())

    def test_short_name(self):
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 's',
            'description': 'valid_description'
        })
        self.assertFalse(user_form.is_valid())

    def test_long_name(self):
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'thisiswaytoomuchofaverylongnamethatshouldnotbeaccepted',
            'description': 'valid_description'
        })
        self.assertFalse(user_form.is_valid())

    def test_long_description(self):
        description = ""
        for i in range(101):
            description = description + "long"
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'thisiswaytoomuchofaverylongnamethatshouldnotbeaccepted',
            'description': description
        })
        self.assertFalse(user_form.is_valid())

    def test_missing_field(self):
        user_form = RegularUserForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'description': 'valid_description'
        })
        self.assertFalse(user_form.is_valid())


class StudentFormTest(TestCase):
    
    def test_valid_student(self):
        user_form = StudentForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'validname',
            'description': 'valid_description',
            'age': 13,
            'gender': 'M',
            'faculty': 'ALU'
        })
        self.assertTrue(user_form.is_valid())

    def test_invalid_age(self):
        user_form = StudentForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'validname',
            'description': 'valid_description',
            'age': 11,
            'gender': 'M',
            'faculty': 'ALU'
        })
        self.assertFalse(user_form.is_valid())

    def test_invalid_gender(self):
        user_form = StudentForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'validname',
            'description': 'valid_description',
            'age': 13,
            'gender': 'A',
            'faculty': 'ALU'
        })
        self.assertFalse(user_form.is_valid())

    def test_invalid_faculty(self):
        user_form = StudentForm({
            'id': 'testuser1',
            'password': 'testpassword1',
            'email': 'email@gmail.com',
            'name': 'validname',
            'description': 'valid_description',
            'age': 13,
            'gender': 'O',
            'faculty': 'FAKE'
        })
        self.assertFalse(user_form.is_valid())
