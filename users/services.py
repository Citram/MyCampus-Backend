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
        description=description_input,
        rating_avg = 3.00
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
        faculty=faculty_input,
        rating_avg = 3.00
    )
    student.save()

def search_users_by_id(id_input):
    '''
    PARTIAL search for a student of which the id CONTAINS the id_input
    '''
    students = Student.objects.all().filter(id__icontains=id_input)
    if len(students) == 0:
        raise UnsuccessfulOperationError('No users exists with that id', 'user_id')
    return students

def get_user_by_id(id_input):
    '''
    EXACT search for a student of which the id MATCHES the id_input
    '''
    try:
        student = Student.objects.get(id=id_input)
    except ObjectDoesNotExist:
        raise UnsuccessfulOperationError ('No user exist with the id ' + id_input, 'id_input')

def search_user_by_name(names):
    students = Student.objects.all()
    for name in names:
        students = students.filter(name__icontains=name)
    if len(students) == 0:
        raise UnsuccessfulOperationError('No users exists with that name', 'name')
    return students

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

def see_student_details(user, age_input, gender_input, faculty_input):
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

def delete_review(review_id):
    try:
        Review.objects.get(id=review_id).delete()
    except ObjectDoesNotExist:
        raise UnsuccessfulOperationError ('No reviews exists with the id ' + review_id, 'review_id')


