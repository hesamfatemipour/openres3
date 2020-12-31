#!/bin/sh
if [ $1 == "uwsgi" ]; then
        shift
        /usr/sbin/uwsgi --http :5000 --wsgi-file middleware.py
fi
