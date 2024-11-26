#!/bin/bash

docker login
docker build --tag edokaa/microoo-transaction:v1.0.0 . -f Dockerfile
docker push edokaa/microoo-transaction:v1.0.0
