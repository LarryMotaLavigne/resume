#!/bin/bash

# Variables
PROJECT_PATH=/MIDDLE
SUPERVISOR_CONF_PATH=/etc/supervisor/conf.d
NGINX_PATH=/etc/nginx

# APP
mkdir ${PROJECT_PATH}
git clone  https://github.com/Squalex/resume.git
cd resume
viurtualenv .
chmod 775 gunicorn_start
source bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# SuperVisor
apt install supervisor
cd ${PROJECT_PATH}/resume
cp B2R/supervisor-resume.conf ${SUPERVISOR_CONF_PATH}/resume.conf
sudo supervisorctl reread
sudo supervisorctl update

# Nginx
apt install nginx
cd ${PROJECT_PATH}/resume
cp B2R/nginx-resume ${NGINX_PATH}/sites-available/resume
sudo ln -s ${NGINX_PATH}/sites-available/resume ${NGINX_PATH}/sites-enabled/resume

sudo service nginx restart