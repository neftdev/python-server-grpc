#!/bin/bash
docker login
docker build -t python-server-grpc .
docker tag python-server-grpc $1/python-server-grpc
docker push $1/python-server-grpc