# I. Intro: Images and Containers

These are my personal notes.

## A. Overview
* `docker build .` : this generates an image from the Dockerfile in the current directory
* `docker run <image>` : this creates a container from the image
### i. Status
* `docker images`
* `docker ps -a` or `docker container ls`
* `docker volume ls`
### ii. Example of building an image
* `docker build -t <name>:<tag> <directory-with-Dockerfile>` : flag "-t" for tag
* `docker build -t goals:latest ./node-app`
### iii. Example of temporal container
* `docker run -p host:docker -d --rm --name <container_name> <image:tag>`
* `docker run -p 3000:80 -d --rm --name goalsapp goals:latest` example

## B. Create an image from Dockerfile
* you need a `Dockerfile`
* then run `docker build .` : which then prints the image hash to your console

## C. Image from container
* `docker ps -a` : show all containers
* `docker images` : show all images
* `docker image inspect <image>`

## D. Ports
* `docker run -p 3000:80 <image>` : host_port(3000):docker_port(80)

## E. Containers
* `docker run <image>` : create a new container from image
* `docker run --rm -d <image>` : the `rm` flag removes container when done; `d` for detached
* `docker start <container>` : starts an existing, previously stopped container
* `docker stop <container>`

## F. Attach, Detach
* `docker run <image>` : generates a new instance of a container
* `docker start <container>` : restarts container, previous stopped
* `docker start -a <container>` : restarts in attached mode
* `docker attach <container>`
* `docker logs <container>` : shows what was printed
* `docker logs -f <id> ` : the "f" flag lets you attach

## G. Docker interactive mode
* `docker run -it <image>` interactive; tty (terminnal), builds from image
* `docker start -a -i <container>` : attaches and runs interactively
### Enter docker container
* `docker exec -it <container> /bin/bash` interactive; tty (terminnal), executes a command on docker
* [link](https://devcoops.com/fix-docker-unable-to-start-container-process-exec-bin-bash/)

## H. Remove
* `docker rm <container>`
* `docker rmi <image>`
* `docker prune <image/container>` : Remove all dangling images (untagged) stopped containers
    * `-a` : Remove all locally stored images

## I. Copy
* `docker cp path/local/. container_name:/path/to/ap`
* `docker cp <source> <target>`

## J. DockerHub
* Login: `docker login` : make your account on DockerHub first
* Share: `docker push <image>`
* Use: `docker pull <image>`

### i. Containers
* `docker run -d --rm --name goals <image> ` : explicitly name the
* `docker run -p 3000:80 -d --rm --name goalsapp goals:latest` example

### ii. Tags
* `docker build -t <name>:<tag> <directory-with-Dockerfile>` : flag:`t` for tag
* `docker build -t goals:latest ./nodejs-app`

# II. Volumes
## A. Status
* `docker volume ls`

## B.
* `docker run -v /app/data` Anonymous volume
* `docker run -v HOST_docker:/app/data` Named olume
* `docker run -v ./HOST/path/to/code:/app/data` Bind Mount volume

![types_of_vols](./img/types_vols_small.png)

# III. Docker Compose 
```
version: "3.8"
services:
  mongodb:
    image: 'mongo'
    volumes: 
      - data:/data/db
    # environment: 
    #   MONGO_INITDB_ROOT_USERNAME: max
    #   MONGO_INITDB_ROOT_PASSWORD: secret
      # - MONGO_INITDB_ROOT_USERNAME=max
    env_file: 
      - ./env/mongo.env
  backend:
    build: ./backend
    # build:
    #   context: ./backend
    #   dockerfile: Dockerfile
    #   args:
    #     some-arg: 1
    ports:
      - '80:80'
    volumes: 
      - logs:/app/logs # named volume
      - ./backend:/app # bind volume
      - /app/node_modules # anonymous volume
    env_file: 
      - ./env/backend.env
    depends_on:
      - mongodb
  frontend:
    build: ./frontend
    ports: 
      - '3000:3000'
    volumes: 
      - ./frontend/src:/app/src # bind volume
    stdin_open: true
    tty: true
    depends_on: 
      - backend

volumes: 
  data: # named volume
  logs: # named volume
```

# IV. Reference
* Source: https://www.udemy.com/course/docker-kubernetes-the-practical-guide/
* Teacher: Maximilian Schwarzmuller