#!/bin/bash
/docker_venv/bin/python ./render.py start &
/docker_venv/bin/gunicorn -c ./gunicorn.conf.py -b :${PORT} wsgi
