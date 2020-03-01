from django.db import models
from hashid_field import HashidAutoField
from django.core.validators import EmailValidator

class User(models.Model):
    """
    Abstract user class which includes admin, students and organizations
    """

    #login info
    ADMIN = 'A'
    USER = 'U'
    PENDING = 'P'
    LOCKED = 'L'
    PRIVILEGE = [
        (ADMIN, 'Admin'),
        (USER, 'Regular User'),
        (PENDING, 'Pending verification'),
        (LOCKED, 'Locked user')
    ]
    privilege = models.CharField(
        max_length=1,
        choices=PRIVILEGE
        )

    id = models.CharField(max_length=20, primary_key=True)

    password = models.CharField(max_length=64)

    email = models.EmailField(null=False, blank=False, unique=True)

    class Meta:
        abstract = True

class Admin(User):
    """
    The admin of the webset with a specific set of pivileges (maybe)
    """

    

class RegularUser(User):
    """
    Regular users of the platform, either a student or an organization
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    rating_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0)

class Student(RegularUser):
    """
    A student or an alumni of McGill
    """

    age = models.PositiveSmallIntegerField()

    #There are only two genders
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        null=True,
        blank=True
    )

    #faculties
    FACULTY_AGRICULTURAL_AND_ENVIRONMENTAL_SCIENCES = 'AGR'
    FACULTY_ARTS = 'ART'
    FACULTY_CONTINUING_STUDIES = 'CNT'
    FACULTY_DENTISTRY = 'DNT'
    FACULTY_EDUCATION = 'EDU'
    FACULTY_ENGINEERING = 'ENG'
    FACULTY_GRADUATE_AND_POSTDOCTORAL_STUDIES = 'GRD'
    FACULTY_LAW = 'LAW'
    FACULTY_MANAGEMENT = 'MNG'
    FACULTY_MEDICINE = 'MED'
    FACULTY_MUSIC = 'MUS'
    FACULTY_SCIENCE = 'SCI'
    ALUMNI = 'ALU'

    FACULTIES = [
        (FACULTY_AGRICULTURAL_AND_ENVIRONMENTAL_SCIENCES, 'Faculty of Agricultural and Environmental Sciences'),
        (FACULTY_ARTS, 'Faculty of Arts'),
        (FACULTY_CONTINUING_STUDIES, 'School of Continuing Studies'),
        (FACULTY_DENTISTRY, 'Faculty of Dentistry'),
        (FACULTY_EDUCATION, 'Faculty of Education'),
        (FACULTY_ENGINEERING, 'Faculty of Engineering'),
        (FACULTY_GRADUATE_AND_POSTDOCTORAL_STUDIES, 'Graduate and Postdoctoral Studies'),
        (FACULTY_LAW, 'Faculty of Law'),
        (FACULTY_MANAGEMENT, 'Desautels Faculty of Management'),
        (FACULTY_MEDICINE, 'Faculty of Medicine'),
        (FACULTY_MUSIC, 'Schulich School of Music'),
        (FACULTY_SCIENCE, 'Faculty of Science'),
        (ALUMNI, 'Alumni'),
    ]

    faculty = models.CharField(
        max_length=3,
        choices=FACULTIES,
        null=True,
        blank=True
    )

    #not sure this is entirely correct
    #following = models.ManyToManyField(RegularUser)

class Organization(RegularUser):
    """
    A club or a student body
    """
    pass

class Review(models.Model):
    """
    An review for an organizer about an event
    """

    #hashed id
    id = HashidAutoField(primary_key=True)

    #rating
    class Rating(models.IntegerChoices):
        """
        ratings for an event, from 1 to 5
        """
        RATING_ONE = 1
        RATING_TWO = 2
        RATING_THREE = 3
        RATING_FOUR = 4
        RATING_FIVE = 5

    rating = models.IntegerField(choices=Rating.choices)

    #comment text
    comment = models.CharField(max_length=300)

    #date & time
    time = models.DateTimeField(auto_now=True)

    #many-to-one relations
    author = models.ForeignKey(Student, on_delete=models.SET('Deleted')) #author of comment deleted, comment stays
    #recepient = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)

class UserFlag(models.Model):
    """
    a flag about another user for an admin to review
    """
    #many-to-one relations
    author = models.ForeignKey(Student, on_delete=models.SET('Deleted'))
    recepient = models.ForeignKey(RegularUser, on_delete=models.CASCADE, related_name='recepient')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='author')

    #hashed id 
    id = HashidAutoField(primary_key=True)

    #TODO
    TYPE1 = '1'
    TYPE2 = '2'

    TYPES = [
        (TYPE1, '1'),
        (TYPE2, '2')
    ]

    flag_type = models.CharField(
        choices=TYPES,
        max_length=1
    )

    details = models.CharField(max_length=300)

    #date & time
    time = models.DateTimeField(auto_now=True)

