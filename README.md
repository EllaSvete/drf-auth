# Lab 29

## Django REST Framework and Docker

### Author

- Ella Svete
- worked with Ben and Eden on this assignment
- I worked on this with help from the class demo

### How to Run this Application

- python3 -m venv .venv
- source .venv/bin/activate
- pip install django
- pip install djangorestframework
- pip install psycopg2-binary
- pip install djangorestframework-simplejwt
- pip install gunicorn
- pip install whitenoise
- django-admin startproject snack_tracker_project
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp snacks
- Make TUV and add to settings
- python manage.py collectstatic

- docker compose up -- build
- docker compose up

- in a separate terminal window run docker compose run web bash
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

### Tests

- to run tests import the class Snacks
- import django.test import APITestCase
- make sure you are in your docker container
- python manage.py test to run tests

- I referenced the tests provided in today's demo

### Overview

- I appreciate the repetition with the labs this week. I am curious how to install auto fill things for django because it so much repetitive typing in each file! 
- Definitely feel like I understand this flow more and more which is great. 

