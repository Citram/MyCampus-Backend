# MyCampus-Backend 

This is the repo for the ECSE428 group project backend.The goal of the project is to develop a platform to help students connect with other students, create events such as sports and social activities, and to have clubs on campus hold their events on their main page for students to participate in.

We'll be using Django and code mostly in Python.

## Requirements
* [Python3](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)
* [MySQL](https://www.mysql.com/)

## Setup

1. Clone this repository in your terminal 

`git clone https://github.com/Citram/MyCampus-Backend.git`

2. Go to the MyCampus-Backend repository

  `cd MyCampus-Backend`
  
3. Set up a virtual environment 

  `pip install virtualenv`
  
  `virtualenv --version`
  
  `virtualenv env`
  
  `pip freeze`
   
  `pip install django`
  
  4. Run the application on server 8080 
  
  `python manage.py runserver 8080`
  
  You'll be able to see the development verison of the application on  `http://localhost:8080/`
  
  You can also access the admin view by going to `http://localhost:8080/admin`

  To get access to the python shell
  
  `python manage.py shell`
  
  Admin log-in information
  
  Django admin: `mycampusbestcampus` password : `ecse428`
