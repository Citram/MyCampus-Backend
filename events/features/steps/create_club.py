@given(u'club <club_name> with club email <club_email> is a club type <club type>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given club <club_name> with club email <club_email> is a club type <club type>')


@when(u'club representative of <club_name> requests a new club in the MyCampus Application System')
def step_impl(context):
    raise NotImplementedError(u'STEP: When club representative of <club_name> requests a new club in the MyCampus Application System')


@then(u'a new club application is generated in the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a new club application is generated in the system')


@then(u'an error message "A club with that club name already exists." is issued')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message "A club with that club name already exists." is issued')


@then(u'an error message "A club with that email already exists." is issued')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message "A club with that email already exists." is issued')


@then(u'an error message "The two password fields didnâ€™t match." is issued')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an error message "The two password fields didnâ€™t match." is issued')
