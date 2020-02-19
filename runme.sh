#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate
python import_data.py
python manage.py runserver&
sleep 5
open http://localhost:8000
