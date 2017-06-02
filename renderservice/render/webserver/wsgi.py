"""WSGI config for render service."""
from render.webserver import application

if __name__ == "__main__":
    application.run()
