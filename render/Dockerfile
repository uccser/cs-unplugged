# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM gcr.io/google-appengine/python

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ARG PROCESS_PORT=8080
ARG FLASK_PRODUCTION=1
ARG PROJECT_NAME=cs-unplugged
ARG QUEUE_NAME=render-queue
ARG API_DISCOVERY_URL
ARG BUCKET_NAME=cs-unplugged-develop
ARG STATIC_DIRECTORY=/render/static

ENV PORT ${PROCESS_PORT}
ENV FLASK_PRODUCTION ${FLASK_PRODUCTION}
ENV PROJECT_NAME ${PROJECT_NAME}
ENV QUEUE_NAME ${QUEUE_NAME}
ENV API_DISCOVERY_URL ${API_DISCOVERY_URL}
ENV STATIC_DIRECTORY ${STATIC_DIRECTORY}

# Install packages (including Weasyprint dependencies), running of Python 3.4.2
RUN apt-get update && apt-get install -y \
      lsb-release \
      build-essential \
      libffi-dev \
      libpq-dev \
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

# Install GCSFUSE
RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s` \
    & echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list \
    & curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    & apt-get update \
    & apt-get install -y \
      gcsfuse

RUN apt-get clean && rm /var/lib/apt/lists/*_*

# Copy and create virtual environment
RUN python -m virtualenv --python=python3.5 /docker_venv

# Set-up file system
RUN mkdir /render
RUN mkdir /render/scripts
COPY ./render/requirements.txt /render
COPY ./render/scripts/pip_install.sh /render/scripts

# Install dependencies
RUN chmod +x /render/scripts/pip_install.sh
RUN /docker_venv/bin/pip3 install -U pip setuptools
RUN /render/scripts/pip_install.sh /docker_venv/bin/pip3 /render/requirements.txt

# Setup Working Directory
ADD ./render /render
WORKDIR /render

EXPOSE ${PORT}

RUN chmod +x /render/scripts/mount-bucket.sh
RUN /render/scripts/mount-bucket.sh ${BUCKET_NAME} ${STATIC_DIRECTORY}

RUN chmod +x /render/scripts/docker-entrypoint.sh
ENTRYPOINT ["/render/scripts/docker-entrypoint.sh"]
