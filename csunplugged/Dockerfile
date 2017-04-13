# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM gcr.io/google-appengine/python

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# Set production settings to false by default.
# For use to production, this can be set to `true` in `docker run --env`
ENV DJANGO_PRODUCTION=false

# Install packages, running of Python 3.4.2
RUN apt-get update && apt-get install -y \
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
RUN pip install -U pip setuptools
RUN python -m virtualenv --python=python3.4 docker_venv
RUN . docker_venv/bin/activate
RUN pip3 install -U pip setuptools
RUN pip3 install packaging
RUN pip3 install appdirs
RUN pip3 install html5lib==1.0b9
RUN pip3 install six
RUN pip3 install weasyprint

# Copy and install Python dependencies
COPY requirements /requirements
# TODO: Figure out how to install different requirements based of env value
RUN pip3 install -r /requirements/local.txt

RUN mkdir /code
WORKDIR /code
ADD ./csunplugged /code/
