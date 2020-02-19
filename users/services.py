from .models import *
from events.services import UnsuccessfulOperationError
from events.models import Event
from django.core.exceptions import ObjectDoesNotExist

def create_admin(user_id, password_input, email_input):
    admin = Admin(privilege='A',id=user_id,password=password_input,email=email_input)
    admin.save()

def create_organization(user_id, password_input, email_input, name_input, description_input):
    organization = Organization(
        privilege='U',
        user=user_id, 
        password=password_input, 
        email=email_input,
        name=name_input,
        description=description_input
    )
    organization.save()
    
def create_student(user_id, password_input, email_input, name_input, description_input, age_input, gender_input, faculty_input):
    student = Student(
        privilege='U',
        id=user_id,
        password=password_input,
        email=email_input,
        name=name_input,
        description=description_input,
        age=age_input,
        gender=gender_input,
        faculty=faculty_input
    )
    student.save()

def search_users_by_id(id_input):
    '''
    PARTIAL search for a student of which the id CONTAINS the id_input
    '''
    users = RegularUser.objects.all().filter(id__icontains=id_input)
    if len(users) == 0:
        raise UnsuccessfulOperationError('No users exists with that id', 'user_id')
    return users

def get_user_by_id(id_input):
    '''
    EXACT search for a student or organization of which the id MATCHES the id_input
    '''
    try:
        user = RegularUser.objects.get(id=id_input)
    except ObjectDoesNotExist:
        raise UnsuccessfulOperationError ('No user exist with the id ' + id_input, 'id_input')
    return user

def search_user_by_name(names):
    users = RegularUser.objects.all()
    for name in names:
        users = users.filter(name__icontains=name)
    if len(users) == 0:
        raise UnsuccessfulOperationError('No users exists with that name', 'name')
    return users

def set_basic_user_details(user, password_input, email_input):
    '''
    user is an object (admin, organization or student)
    this resets the password and the email
    '''
    user.password = password_input
    user.email = email_input
    user.save()

def set_regular_user_details(user, name_input, description_input):
    '''
    user is an object (organization or student)
    this resets the name and description for a regular user
    '''
    user.name = name_input
    user.description = description_input
    user.save()

def set_student_details(user, age_input, gender_input, faculty_input):
    '''
    user is an object (student)
    this resets the name and description for a regular user
    '''
    user.age = age_input
    user.gender = gender_input
    user.faculty = faculty_input
    user.save()


#============================= Review services ==================================#
def create_review(user_id, event_id, rating_input, comment_input):
    user = get_user_by_id(user_id)
    try:
        event = Event.objects.get(event_id)
    except ObjectDoesNotExist:
        raise UnsuccessfulOperationError ('No event exists with the id ' + event_id, 'event_id')
    review = Review(rating=rating_input, comment=comment_input)
    review.author=user
    review.event=event
    review.save()
    #update rating
    rating_sum = 0
    for review in user.reviews:
        rating_sum += review.rating
    avg = float("{0:.2f}".format(rating_sum/len(user.reviews)))
    user.rating_avg = avg
    user.save()

def delete_review(user_id, review_id):
    #check review exists
    try:
        review = Review.objects.get(id=review_id)
    except ObjectDoesNotExist:
        raise UnsuccessfulOperationError ('No reviews exists with the id ' + review_id, 'review_id')
    #check author
    if user_id != review.author.id:
        raise UnsuccessfulOperationError ('You cannot delete this review', 'user_id')
    review.delete()


    

