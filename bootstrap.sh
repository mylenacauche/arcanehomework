#!/bin/sh
export FLASK_APP=./apiproject/index.py
source $(pipenv --venv)/Scripts/activate
flask run