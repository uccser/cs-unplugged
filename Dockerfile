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
      python3-pip
RUN apt-get clean && rm /var/lib/apt/lists/*_*

# Copy and install Python dependencies
COPY requirements /requirements
# TODO: Figure out how to install different requirements based of env value
RUN pip3 install -r /requirements/local.txt
RUN pip3 install -r /requirements/kordac.txt
RUN pip3 install git+git://github.com/uccser/kordac.git

RUN mkdir /code
WORKDIR /code
ADD ./csunplugged /code/
