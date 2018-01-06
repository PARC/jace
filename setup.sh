#!/bin/bash
apk update
apk add py3-psycopg2
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations user_model
python manage.py migrate
python manage.py test user_model


