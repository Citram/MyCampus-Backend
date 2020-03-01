@given(u'A user <user_id> is logged into his account')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given A user <user_id> is logged into his account')


@when(u'He wants to comment a string <str> on a posted event <evt_id> as <user_id>')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: When He wants to comment a string <str> on a posted event <evt_id> as <user_id>')


@then(u'A comment is added to the system attached to the posted event <evt_id>')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then A comment is added to the system attached to the posted event <evt_id>')


@given(u'A user <user_id> is not logged into his account')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given A user <user_id> is not logged into his account')


@when(u'He wants to comment a string <str> on a posted event <evt_id> as <user2_id>')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: When He wants to comment a string <str> on a posted event <evt_id> as <user2_id>')


@then(u'The user is redirected to a page indicating unauthorised access')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then The user is redirected to a page indicating unauthorised access')


@given(u'<user2_id> does not exist')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given <user2_id> does not exist')


@then(u'The user is redirected to a page indicating non-existent user')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then The user is redirected to a page indicating non-existent user')


@given(u'<evt_id> does not exist')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given <evt_id> does not exist')


@then(u'The user is redirected to a page indicating non-existent event')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then The user is redirected to a page indicating non-existent event')

