# Flask REST demo with Auth

The purpose of this repo is only to demonstrate how to build a simple REST API (Blog and authorization) with Flask.

## What's included?

 1. MySQL support
 2. Migrations
 3. Authorization with JWT key
 4. Flask-RestPlus integration
 5. Swagger UI 

## Installation

I recommend using `virtualenv` and `virtualenvwrapper` to isolate packages.

Use pip to install the packages in the requirements file:
```
$ pip install -r requirements.txt
```

## Initializing the db

To run the app, the database must be initialized:
```
$ set FLASK_APP=rest_demo/run.py
$ flask db upgrade
```

## Running the app

Just run the included script using python:
```
$ python rest_demo/run.py
```