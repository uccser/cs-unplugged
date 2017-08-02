#!/bin/bash

docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker-compose build

django_image="csu-django"
django_version="local-2.0.0-alpha.4"

nginx_image="csu-nginx"
nginx_version="1.0.1"

docker tag $DOCKER_USERNAME/$django_image:$django_version $DOCKER_USERNAME/$django_image:latest
docker tag $DOCKER_USERNAME/$nginx_image:$nginx_version $DOCKER_USERNAME/$nginx_image:latest

# push it
docker push $DOCKER_USERNAME/$django_image:latest
docker push $DOCKER_USERNAME/$django_image:$django_version

docker push $DOCKER_USERNAME/$nginx_image:latest
docker push $DOCKER_USERNAME/$nginx_image:$nginx_version
