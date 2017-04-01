#!/bin/bash

export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_USER

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_USER", user="$POSTGRES_USER", password="$POSTGRES_PASSWORD", host="postgres")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Load topics content
echo "Load topics content"
python3 manage.py updatedata

# Start gunicorn service
echo "Starting gunicorn"
gunicorn -c gunicorn.conf.py -b :$PORT config.wsgi
