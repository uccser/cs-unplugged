"""Configuration file for gunicorn."""
import multiprocessing

# Details from https://cloud.google.com/appengine/docs/flexible/python/runtime
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-APPENGINE-HTTPS': 'on'}
