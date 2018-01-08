#!/bin/bash
#Sets up jace
apk update
apk add libpq-dev python3-dev
apk add postgresql-server-dev-all
apk add py3-psycopg2
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations user_model
python3 manage.py migrate
python3 manage.py test user_model


