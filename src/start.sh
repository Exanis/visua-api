#!/bin/bash

python manage.py migrate
(echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${ADMIN_USER}', '${ADMIN_EMAIL}', '${ADMIN_PASSWORD}')" | python manage.py shell) | true

gunicorn -w 4 visua.wsgi -b 0.0.0.0:80 --threads 4