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
      python-psycopg2 \
      python3 \
      python3-pip \
      python3-dev \
      # Install wkhtmltopdf
      openssl \
      build-essential \
      xorg \
      libssl-dev
RUN apt-get -y clean

# Install wkhtmltopdf 0.12.4
RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar -xJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
WORKDIR wkhtmltox
RUN chown root:root bin/wkhtmltopdf
RUN cp -r * /usr/
WORKDIR /app

# Copy and install Python dependencies
COPY requirements /requirements
# TODO: Figure out how to install different requirements based of env value
RUN pip3 install -r /requirements/local.txt
RUN pip3 install -r /requirements/kordac.txt
RUN pip3 install git+git://github.com/uccser/verto.git
RUN mkdir /code
WORKDIR /code
ADD ./csunplugged /code/
