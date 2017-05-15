FROM nginx:latest

# Install Node.js and other dependencies
RUN apt-get update && \
    apt-get -y install curl gnupg2 && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get -y install python build-essential nodejs
WORKDIR /app
RUN npm install --global gulp-cli
RUN npm install --global node-gyp
RUN apt-get update && apt-get install -y \
      libcairo2-dev \
      libjpeg-dev \
      libpango1.0-dev \
      libgif-dev \
      g++
ADD csunplugged/package.json /app/
RUN npm install
ADD ./csunplugged/ /app/
ADD infrastructure/nginx/nginx.conf /etc/nginx/nginx.conf
