"""WSGI config for render service."""
from render.webserver.app import application

if __name__ == "__main__":
    application.run()
