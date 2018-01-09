#!/bin/bash
#Runs jace, and starts the scheduler
run_local.sh
./manage.py run_huey
