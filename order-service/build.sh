#!/bin/bash

docker login
docker build --tag edokaa/microoo-order:v1.0.0 . -f Dockerfile
docker push edokaa/microoo-order:v1.0.0
