#!/bin/bash

cd /MIDDLE/resume
virtualenv .
source bin/activate
pip3 install -r requirements.txt

mkdir /MIDDLE/resume/run
mkdir /MIDDLE/resume/logs