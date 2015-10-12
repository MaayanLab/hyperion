#!/usr/bin/env bash

DOCKER_IMAGE="maayanlab/hyperion:$1"
echo $DOCKER_IMAGE
boot2docker init
boot2docker up
boot2docker shellinit
docker build -t $DOCKER_IMAGE .
docker push $DOCKER_IMAGE