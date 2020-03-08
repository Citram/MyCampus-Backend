from behave import *
from users.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


use_step_matcher("parse")

g_userform = None

@given(u'student with username <username>')
def step_impl(context):
    pass

@when(u'student <username> with password <password> requests user access to the MyCampus Application System')
def step_impl(context):
    create_user(context)

@when(u'student <username> with duplicate username requests user access to the MyCampus Application System')
def step_impl(context):
    create_user(context)

@when(u'student <username> with non-matching passwords requests user access to the MyCampus Application System')
def step_impl(context):
    create_user(context)

@then(u'a new user with username <username> is generated in the system')
def step_impl(context):
    users = User.objects.all()
    assert len(users) == len(context.table.rows)
    for idx, row in enumerate(context.table):
        user = users[idx]
        assert user.username == row['username']


@then(u'a error message "{error}" is issued')
def step_impl(step, error):
    global g_userform
    assert g_userform.is_valid() == False
    print(g_userform.errors)
    assert error in str(g_userform.errors)

def create_user(context):
    global g_userform
    for row in context.table:
        user = {}
        user['username'] = row['username']
        user['password1'] = row['password']
        user['password2'] = row['password2']
        user_form = UserCreationForm(user)
        if (user_form.is_valid()):
            user_form.save()
        g_userform = user_form
        