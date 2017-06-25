FROM nginx:latest

# Populate sources with closest neighbours
# Resolves issues with failing builds, should be removed in future
RUN apt-get update \
    && apt-get install -y netselect-apt --no-install-suggests \
    && netselect-apt stretch \
    && mv sources.list /etc/apt/sources.list

# Install Node.js and other dependencies
RUN apt-get autoremove
    && apt-get update \
    && apt-get install --no-install-suggests -y \
        curl \
        gnupg2 \
        python \
        build-essential \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install --no-install-suggests -y \
        nodejs \
    && apt-get remove --purge -y gnupg2 && apt-get -y --purge autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN npm install --global gulp-cli node-gyp
RUN apt-get update \
    && apt-get install --no-install-suggests -y \
       libcairo2-dev \
       libjpeg-dev \
       libpango1.0-dev \
       libgif-dev \
       g++ \
    && rm -rf /var/lib/apt/lists/*

ADD csunplugged/package.json /app/
RUN npm install
ADD ./csunplugged/ /app/
ADD infrastructure/nginx/nginx.conf /etc/nginx/nginx.conf
