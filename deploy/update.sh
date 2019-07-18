#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/Users/apple/Developer/python/new_rises'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart rises_api

echo "DONE! :)"
