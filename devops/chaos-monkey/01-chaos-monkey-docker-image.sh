#!/bin/bash

# Create a new Dockerfile
touch Dockerfile
echo "FROM python:3.8-slim-buster

COPY chaos-monkey.py /app/chaos-monkey.py

RUN pip install kubernetes schedule

CMD ["python", "/app/chaos-monkey.py"]" > Dockerfile

# Build the Docker image
docker build -t milisucevic/chaos-monkey:1.0.0 .

# Push Docker Image to Docker Hub
docker push milisucevic/chaos-monkey:1.0.0 

