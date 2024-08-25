#!/bin/bash

# Define variables
IMAGE_NAME="honeypot.dockerfile"
CONTAINER_NAME="HoneyPotContainer"
LOGS_DIR="$(pwd)/logs"

# Create logs directory if it doesn't exist
if [ ! -d "$LOGS_DIR" ]; then
  mkdir -p "$LOGS_DIR"
fi

# Build the Docker image
docker build -t $IMAGE_NAME .

# Stop and remove any existing container with the same name
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# Run the Docker container with persistent storage for logs
docker run -d --name $CONTAINER_NAME -p 5000:5000 -v $LOGS_DIR:/app/logs $IMAGE_NAME
