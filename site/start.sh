#!/bin/bash

IMAGE=kubernetes-failure-stories
docker build -t $IMAGE .
docker run -d --name kubernetes-failure-stories -u $(id -u) -v /var/www/k8s.af/workdir:/workdir --restart=always $IMAGE
