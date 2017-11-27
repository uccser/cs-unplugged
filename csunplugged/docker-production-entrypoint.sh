export DJANGO_SETTINGS_MODULE="config.settings.production"

echo "Compiling message files"
/docker_venv/bin/python3 ./manage.py compilemessages

# Start gunicorn service
echo "Starting gunicorn"
/docker_venv/bin/gunicorn -c ./gunicorn.conf.py -b :$PORT config.wsgi --reload
