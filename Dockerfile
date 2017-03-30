# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM gcr.io/google-appengine/python

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# ============================================================================
# SETTINGS
# ----------------------------------------------------------------------------
# Enable production settings by default; for development, this can be set to
# `false` in `docker run --env`
ENV DJANGO_PRODUCTION=true
# ============================================================================

# Install packages, running of Python 3.4.2
RUN apt-get update && apt-get install -y \
      python3 \
      python3-dev \
      postgresql \
      python-psycopg2 \
      libpq-dev \
      nginx \
      supervisor
