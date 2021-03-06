#!/bin/bash

source nn-venv/bin/activate
python imagerecognition/manage.py runserver

# open Django REST framework webpage at http://127.0.0.1:8000/api/ 