#!/bin/bash

PROJECT_PATH=/MIDDLE/resume
PROJECT_NAME=resume
# Stop the Supervisor service
sudo supervisorctl stop ${PROJECT_NAME}

cd ${PROJECT_PATH}
git pull

# Database Migration
python3 manage.py makemigrations --settings=resume.settings.production
python3 manage.py migrate --settings=resume.settings.production
python3 manage.py makemigrations core --settings=resume.settings.production
python3 manage.py migrate core --settings=resume.settings.production

# For db.sqlite (for the moment)
chmod 777 db.sqlite3


chmod 775 gunicorn_start
sudo supervisorctl restart ${PROJECT_NAME}



