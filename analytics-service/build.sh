#!/bin/bash

docker login
docker build --tag edokaa/microoo-analytics:v1.0.0 . -f Dockerfile
docker push edokaa/microoo-analytics:v1.0.0
