#!/bin/bash

docker login
docker build --tag edokaa/microoo-notification:v1.0.0 . -f Dockerfile
docker push edokaa/microoo-notification:v1.0.0
