FROM debian:jessie
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Arguments and Environment Variables
ARG DEBIAN_FRONTEND=noninteractive
ARG PROCESS_PORT=5000
ENV PORT ${PROCESS_PORT}

# Install packages
RUN apt-get update && apt-get install -y \
      python3 \
      python3-dev \
      python3-pip \
      python3-venv
RUN apt-get clean && rm /var/lib/apt/lists/*_*

# Copy and create virtual environment
RUN python3 -m venv /docker_venv

# Install dependencies
COPY infrastructure/queue/requirements.txt /
RUN /docker_venv/bin/pip3 install -U pip setuptools
RUN /docker_venv/bin/pip3 install -r /requirements.txt

# Setup Working Directory
RUN mkdir /queue
ADD ./infrastructure/queue /queue
WORKDIR /queue

EXPOSE ${PORT}

CMD /docker_venv/bin/gunicorn -c ./gunicorn.conf.py -b :${PORT} wsgi
