#!/bin/bash

source .python/bin/activate
DATABASE_URL=postgres://cuzgqcdpvhhscp:NB2cFNcDdegvYcJX9aEQpxqzOk@ec2-54-197-240-180.compute-1.amazonaws.com:5432/d7ch3acbco3jhc DJANGO_SETTINGS_MODULE=app.settings python manage.py syncdb

