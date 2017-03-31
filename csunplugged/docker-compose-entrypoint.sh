#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Load topics content
echo "Load topics content"
python3 manage.py updatedata

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
