@given(u'student with username "mycampus1" is logged in')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Given student with username "mycampus1" is logged in')


@when(u'student requests to change password to "android1234"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student requests to change password to "android1234"')


@when(u'student is enters old password "android1298"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student is enters old password "android1298"')


@then(u'the password of "mycampus1" is updated to "android1234"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then the password of "mycampus1" is updated to "android1234"')


@when(u'student requests to change password to "test2@mail.mcgill.ca"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student requests to change password to "test2@mail.mcgill.ca"')


@then(u'the email of "mycampus1" is updated to "test2@mail.mcgill.ca"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then the email of "mycampus1" is updated to "test2@mail.mcgill.ca"')


@when(u'student is enters old password "android1234"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student is enters old password "android1234"')


@then(u'the error message "Please enter the correct confirmation password" is issued')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then the error message "Please enter the correct confirmation password" is issued')


@when(u'student requests to change password to "abcd"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student requests to change password to "abcd"')


@then(u'the error message "Password is too short." is issued')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then the error message "Password is too short." is issued')


@when(u'student requests to change password to "test2@gmail.com"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When student requests to change password to "test2@gmail.com"')


@then(u'the error message "Only @mail.mcgill.ca emails are permitted." is issued')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then the error message "Only @mail.mcgill.ca emails are permitted." is issued')