#!/usr/bin/env bash
python find_and_kill_server.py
python manage.py runserver&
sleep 5
open http://localhost:8000