FROM ghcr.io/uccser/django:2.2.19-1

# Set terminal to be noninteractive
ENV DJANGO_PRODUCTION=False

# Install dependencies
COPY --chown=uccser:uccser requirements/ requirements/
RUN /docker_venv/bin/pip3 install -r requirements/local.txt

# Copy and install fonts
COPY --chown=uccser:uccser csunplugged/static/fonts/ /usr/share/fonts/
RUN fc-cache -fv

CMD [ "/app/docker-development-entrypoint.sh" ]
