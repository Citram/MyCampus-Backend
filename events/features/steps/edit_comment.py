@given(u'user <user_name> is user id <user_id> is of status <user_status> logged in')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given user <user_name> is user id <user_id> is of status <user_status> logged in')


@when(u'user <user_name> requests modification of a comment with id <comment_id>')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: When user <user_name> requests modification of a comment with id <comment_id>')


@when(u'content <comment_content>')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: When content <comment_content>')


@then(u'the content is updated to <comment_content> in the system')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then the content is updated to <comment_content> in the system')


@given(u'"George Pig" is logged out')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given "George Pig" is logged out')


@when(u'"George Pig" requests modification of a comment with id')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: When "George Pig" requests modification of a comment with id')


@then(u'a "You must be logged in to delete a comment :(" message is issued')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then a "You must be logged in to delete a comment :(" message is issued')


