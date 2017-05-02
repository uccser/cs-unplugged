# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM gcr.io/google-appengine/python

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ARG PROCESS_PORT=8080
ARG FLASK_PRODUCTION=1

ENV PORT ${PROCESS_PORT}
ENV FLASK_PRODUCTION=${FLASK_PRODUCTION}

# Install packages (including Weasyprint dependencies), running of Python 3.4.2
RUN apt-get update && apt-get install -y \
      build-essential \
      libffi-dev \
      libpq-dev \
      nginx \
      python-psycopg2 \
      python3 \
      python3-dev \
      python3-pip \
      libcairo2-dev \
      python-dev \
      python-pip \
      python-lxml \
      python-cffi \
      libpango1.0-0 \
      libgdk-pixbuf2.0-0 \
      shared-mime-info
RUN apt-get clean && rm /var/lib/apt/lists/*_*

# Copy and create virtual environment
RUN python -m virtualenv --python=python3.5 /docker_venv

# Install dependencies
RUN mkdir /requirements
COPY requirements.txt /requirements
COPY pip_install.sh /requirements

RUN chmod +x /requirements/pip_install.sh
RUN /docker_venv/bin/pip3 install -U pip setuptools
RUN /requirements/pip_install.sh /docker_venv/bin/pip3 /requirements/requirements.txt

# Setup Working Directory
RUN mkdir /render
ADD . /render
WORKDIR /render

EXPOSE ${PORT}

CMD /docker_venv/bin/gunicorn -c gunicorn.conf.py -b :${PORT} app:app
