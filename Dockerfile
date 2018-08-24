FROM uccser/django:1.11.14

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ENV DJANGO_PRODUCTION=True

EXPOSE 8080
RUN mkdir /csunplugged
WORKDIR /csunplugged

# Copy and install Python dependencies
COPY requirements /requirements
RUN /docker_venv/bin/pip3 install -r /requirements/production.txt

ADD ./csunplugged /csunplugged/

CMD /csunplugged/docker-production-entrypoint.sh
