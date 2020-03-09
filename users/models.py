from django.db import models
from django import forms
from hashid_field import HashidAutoField
#from events.models import *

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
    class Meta:
        abstract = False

class RegularUser(User):
    """
    Regular users of the platform, either a student or an organization
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

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

    class Meta:
        abstract = False

    #not sure this is entirely correct
    #following = models.ManyToManyField(RegularUser)

class Organization(RegularUser):
    """
    A club or a student body
    """
    class Meta:
        abstract = False