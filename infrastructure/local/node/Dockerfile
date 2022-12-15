FROM node:14.17.0-buster

ARG DOCKER_UID=1000
RUN usermod -u $DOCKER_UID node

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    g++ \
    libcairo2-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libpng-dev \
    libgif-dev \
    librsvg2-dev \
    make \
    python \
    # Cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN chown -R node:node /app

USER node
RUN mkdir /app/build
COPY --chown=node:node ./csunplugged/package.json /app
RUN npm install && npm cache clean --force
ENV PATH ./node_modules/.bin/:$PATH
