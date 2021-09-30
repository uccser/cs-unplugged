FROM python:3.9.5-slim-buster as python

# Python build stage ----------------------------------------------------------
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=production

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt

# Python run stage ------------------------------------------------------------
FROM python as python-run-stage

ARG GIT_SHA
ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

# Set environment variables
ENV LANG C.UTF-8
ENV DEPLOYED=True
ENV DJANGO_SETTINGS_MODULE='config.settings.production'
ENV GIT_SHA ${GIT_SHA}
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django && adduser --system --ingroup django django

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # Healthcheck tool
    curl \
    # Cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction.
# All relative dir copies are wrt to the workdir instruction.
# Copy python dependency wheels from python-build-stage
# and then use wheels to install Python dependencies.
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY --chown=django:django ./infrastructure/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./infrastructure/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy application code to WORKDIR
COPY --chown=django:django /csunplugged/ ${APP_HOME}
# Make django owner of the WORKDIR directory as well.
RUN chown django:django ${APP_HOME}

USER django

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=30s --start-period=5s --retries=3 \
    CMD curl --fail --silent http://localhost:8000/healthcheck/ || exit 1

ENTRYPOINT ["/entrypoint"]
CMD ["/start"]
