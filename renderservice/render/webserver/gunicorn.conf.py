"""Configuration file for gunicorn."""
import multiprocessing

# Details from https://cloud.google.com/appengine/docs/flexible/python/runtime
timeout = 10
graceful_timeout = 30
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-APPENGINE-HTTPS': 'on'}

# Logging
accesslog = 'access.log'
