# Restful Api

This is a Restfull API Built with Python, Django & Django Rest Frameworks.

## Running this App

Before Running, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.
Clone the app

Kindly ensure that you are in the project directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Start server

    Open another terminal window, activate the virtual environment and run the following command:

    . env/bin/activate && python manage.py runserver 8080
