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
ARG STATIC_DIRECTORY=/renderservice/static

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
      openssl \
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
    && echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y \
      gcsfuse \
    && apt-get clean && rm /var/lib/apt/lists/*_*

# Copy and create virtual environment
RUN python -m virtualenv --python=python3.5 /docker_venv

# Set-up file system
RUN mkdir /renderservice \
    && mkdir /renderservice/scripts
COPY ./renderservice/requirements.txt /renderservice
COPY ./renderservice/scripts/pip-install.sh /renderservice/scripts

# Install dependencies
RUN chmod +x /renderservice/scripts/pip-install.sh \
    && /docker_venv/bin/pip3 install -U pip setuptools \
    && /renderservice/scripts/pip-install.sh /docker_venv/bin/pip3 /renderservice/requirements.txt

# Setup Working Directory
ADD ./renderservice /renderservice
WORKDIR /renderservice

# Setup User
RUN useradd -c "RenderService user" -m -d /home/render -s /bin/bash render \
    && chown -R render.render /render
USER render
ENV HOME /home/render

EXPOSE ${PORT}

# Mount Bucket
RUN chmod +x /renderservice/scripts/mount-bucket.sh
RUN /renderservice/scripts/mount-bucket.sh ${BUCKET_NAME} ${STATIC_DIRECTORY}

# Run System
RUN chmod +x /renderservice/scripts/docker-entrypoint.sh
ENTRYPOINT ["/renderservice/scripts/docker-entrypoint.sh"]
