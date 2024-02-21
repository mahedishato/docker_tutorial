# Docker Tutorial

Welcome to the Docker Tutorial repository! This tutorial covers the basics of Docker, containerization, and how to work with Docker containers.

## Table of Contents
1. [Introduction to Docker](#introduction-to-docker)
2. [Installation](#installation)
3. [Docker Commands](#docker-commands)
   - [Build an Image](#build-an-image)
   - [Run a Container](#run-a-container)
   - [List Containers](#list-containers)
   - [Stop and Remove a Container](#stop-and-remove-a-container)
   - [Docker Images](#docker-images)
4. [Docker Compose](#docker-compose)
5. [Dockerfile](#dockerfile)
6. [Conclusion](#conclusion)

## Introduction to Docker
Docker is a platform that enables developers to automate the deployment of applications inside lightweight, portable containers.

## Installation
Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) to install Docker on your machine.

## Docker Commands

### Build an Image
To build a Docker image from a Dockerfile, use the following command:
```bash
docker build -t image_name:tag path/to/Dockerfile


### Run a Container
To run a container from an image, use the following command:
```bash
docker run -d -p 8080:80 --name my_container image_name:tag
```

### List Containers
To list running containers, use the following command:
```bash
docker ps
```

### Stop and Remove a Container
To stop and remove a running container, use the following commands:
```bash
docker stop my_container
docker rm my_container
```

### Docker Images
To list existing Docker images, use the following command:
```bash
docker images
```

## Docker Compose
Docker Compose is a tool for defining and running multi-container Docker applications. Create a `docker-compose.yml` file to specify the services, networks, and volumes for your application.

Example `docker-compose.yml`:
```yaml
version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

To run the services defined in `docker-compose.yml`, use the following command:
```bash
docker-compose up -d
```

## Dockerfile
A Dockerfile is a script that contains instructions to build a Docker image. It defines the base image, environment variables, and commands to run during image creation.

Example `Dockerfile`:
```Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3
CMD ["python3", "-m", "http.server", "80"]
```

## Conclusion
Congratulations! You've completed the basic Docker tutorial. Explore more advanced features and best practices in the [official Docker documentation](https://docs.docker.com/).

Feel free to contribute to this tutorial by opening issues or pull requests. Happy Dockerizing!
