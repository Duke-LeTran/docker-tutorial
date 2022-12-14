# I. Intro: Images and Containers

These are my personal notes.

## A. Overview
* `docker build .` : this generates an image from the Dockerfile in the current directory
* `docker run <image>` : this creates a container from the image
* `docker start <container>` : this starts an existing container
* `docker compose up -d` : this turns on all the services of a `docker-compose.yml` file


### ii. Status
* `docker images`
* `docker container ls` or `docker ps -a`
* `docker volume ls`

### ii. Example of building an image
* `docker build -t <name>:<tag> <directory-with-Dockerfile>` : flag "-t" for tag
* `docker build -t goals:latest ./node-app` example

### iii. Example of temporal container
* `docker run -p host:docker -d --rm --name <container_name> <image:tag>`
* `docker run -p 3000:80 -d --rm --name goalsapp goals:latest` example

## B. Create an image from Dockerfile
* you need a `Dockerfile` to build an image
* then run `docker build .` : which then prints the image hash to your console

## C. Image from container
* `docker ps -a` : show all containers
* `docker images` : show all images
* `docker image inspect <image>` : show more details about the image

## D. Ports
* `docker run -p 3000:80 <image>` : host_port(3000):docker_port(80)

## E. Containers
* `docker run <image>` : create a new container from image
* `docker run --rm -d <image>` : some useful flags
    * the `rm` flag removes container when done
    * the `d` flag for detached
* `docker start <container>` : starts an existing, previously stopped container
* `docker stop <container>`

## F. Attach, Detach
* `docker run <image>` : generates a new instance of a container
* `docker start <container>` : restarts container, previous stopped
* `docker start -a <container>` : restarts in attached mode
* `docker attach <container>` : attaches to container
* `docker logs <container>` : shows what was printed
* `docker logs -f <id> ` : the "f" flag lets you attach

## G. Docker interactive mode
* `docker run -it <image>` interactive; tty (terminnal), builds from image
* `docker start -a -i <container>` : attaches and runs interactively
### Enter docker container
* `docker exec -it <container> /bin/bash` interactive; tty (terminnal), executes a command on docker
* [more info link](https://devcoops.com/fix-docker-unable-to-start-container-process-exec-bin-bash/)

## H. Remove
* `docker rm <container>` : remove container
* `docker rmi <image>` : remote image
* `docker prune <image/container>` : remove all dangling images (untagged) stopped containers
    * `-a` : remove all locally stored images

## I. Copy
* `docker cp path/local/. container_name:/docker_path/to/ap`
* `docker cp <source> <target>`

## J. DockerHub
* Login: `docker login` : make your account on DockerHub first
* Share: `docker push <image>` : push to repository
* Use: `docker pull <image>` : pull from repository

## K. Temporal Containers
* `docker run -d --rm --name goals <image> ` : explicitly name the
* `docker run -p 3000:80 -d --rm --name goalsapp goals:latest` example

## L. Tags
* `docker build -t <name>:<tag> <directory-with-Dockerfile>` : flag:`t` for tag
* `docker build -t goals:latest ./node-app` : example of file

# II. Volumes
## A. Status
* `docker volume ls`

## B.
* `docker run -v /app/data` Anonymous volume
* `docker run -v HOST_docker:/docker_app/data` Named olume
* `docker run -v ./HOST/path/to/code:/docker_app/data` Bind Mount volume

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
# VI. Installation
* Amazon Linux 2: https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9
* Amazon Linux Extras: https://aws.amazon.com/premiumsupport/knowledge-center/ec2-install-extras-library-software/
* Windows (Desktop): https://docs.docker.com/desktop/install/windows-install/
* Ubuntu (Engine): https://docs.docker.com/engine/install/ubuntu/

# V. More useful Docker documentation
* https://docs.docker.com/compose/
* https://docs.docker.com/compose/compose-file/
* https://hub.docker.com/_/python/
* https://github.com/docker/awesome-compose

# V. Reference
* Source: https://www.udemy.com/course/docker-kubernetes-the-practical-guide/
* Teacher: Maximilian Schwarzmuller