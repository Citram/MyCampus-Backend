from behave import *
from create_new_user import create_user
from django.contrib.auth import authenticate

g_user = None

@given(u'the following users are in the system')
def step_impl(context):
    create_user(context)

@when(u'student "{user}" with password "{password}" requests user access to the MyCampus Application System')
def step_impl(step, user, password):
    global g_user
    g_user = authenticate(username=user, password=password)

@then(u'the system should authenticate the student')
def step_impl(context):
    assert g_user is not None

@then(u'the system should not authenticate the user')
def step_impl(context):
    assert g_user is None
