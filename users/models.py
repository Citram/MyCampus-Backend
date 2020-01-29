from django.db import models
from django import forms
from hashid_field import HashidAutoField
from events.models import Event


# Create your models here.
class User(models.Model):

    id = models.CharField(max_length=20, primary_key=True)

    password = models.CharField(max_length=64, widget=forms.PasswordInput)

    email = models.EmailField(null=False, blank=False, unique=True)

    class Meta:
        abstract = True

class Admin(User):
    privilege = models.IntegerField()

class RegularUser(User):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    class Meta:
        abstract = True

class Student(RegularUser):

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
        (FACULTY_ENGINEERING, 'FACULTY_EDUCATION'),
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
    following = models.ManyToManyField(RegularUser)

class Organization(RegularUser):
    pass

class Review(models.Model):

    #hashed id 
    id = HashidAutoField(primary_key=True)

    #rating
    class Rating(models.IntegerChoices):

        RATING_ONE = 1
        RATING_TWO = 2
        RATING_THREE = 3
        RATING_FOUR = 4
        RATING_FIVE = 5

    rating = models.IntegerField(choices=Rating.choices)

    #comment text
    comment = models.CharField(max_length=300)

    #many-to-one relations
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    recepient = models.ForeignKey(RegularUser, on_delete=models.CASCADE)

class Report(models.Model):

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

    #many-to-one relations
    author = models.ForeignKey(Student,on_delete=models.CASCADE)
    recepient = models.ForeignKey(Student, on_delete=models.CASCADE)


