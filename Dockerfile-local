FROM uccser/django:1.11.14-with-weasyprint

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive

ENV DJANGO_PRODUCTION=False
EXPOSE 8080

# Copy and create virtual environment
COPY requirements /requirements

# Install dependencies
RUN /docker_venv/bin/pip3 install -r /requirements/local.txt

RUN mkdir /cs-unplugged/
RUN mkdir /cs-unplugged/csunplugged/
WORKDIR /cs-unplugged/csunplugged/

# Copy and install fonts
COPY csunplugged/static/fonts/ /usr/share/fonts/
RUN fc-cache -fv
