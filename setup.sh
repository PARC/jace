#!/bin/bash
apk update
apk add py3-psycopg2
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations user_model
python3 manage.py migrate
./run_local
python3 manage.py run_huey

