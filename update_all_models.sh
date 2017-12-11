#!/bin/bash
python manage.py makemigrations user_model
python manage.py makemigrations communications
python manage.py migrate
python manage.py test user_model
