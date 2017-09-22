#!/bin/bash
python manage.py makemigrations user_model
python manage.py makeigrations communications
python manage.py migrate
python manage.py test user_model
