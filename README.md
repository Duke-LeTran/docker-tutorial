

# I. Intro: Images and Containers
## A. Overview
* `docker build .` : this generates an image from the Dockerfile
* `docker run <image>` : this creates a container from the image
* `docker ps -a` or `docker container ls`
* `docker images`

## B. Create an image
* you need a `Dockerfile`
* then run `docker build .` : which then prints the image to your 

## C. Image from container
* `docker ps -a` : show all containers
* `docker images` : show all images
* `docker image inspect <image>`

## D. Ports
* `docker run -p 3000:80 <image>` : host_port(3000):docker_port(80)

## E. Containers
* `docker run <image>` : create a new container from image
* `docker run --rm -d <image>` : flag:`rm` remove container when done; `d` detached
* `docker start <container>`
* `docker stop <container>`

## F. Attach, Detach
* `docker run -p 8000:80 <container>` : run with a port
* `docker run` : generates a new 
* `docker start` : restarts container, previous stopped
* `docker start -a` : restarts in attached mode
* `docker attach <container>`
* `docker logs <container>` : shows what was printed
* `docker logs -f <id> ` : the f flag lets you attach


## G. Docker interactive mode
* `docker run -it <image>` interactive; tty (terminnal), builds from image
* `docker start -a -i <container>` : attaches and runs interactively
### Enter docker container
`docker exec -it <container> /bin/bash`
#docker compose exec {image} /bin/bash
https://devcoops.com/fix-docker-unable-to-start-container-process-exec-bin-bash/

## H. Remove
* `docker rm <container>`
* `docker rmi <image>`
* `docker prune <image/container>` : Remove all dangling images (untagged) stopped containers
    * `-a` : Remove all locally stored images

## I. Copy
* `docker cp path/local/. container_name:/path/to/ap`
* `docker cp <source> <target>`

## J. DockerHub
* Share: `docker push <image>`
* Use: `docker pull <image>`

### i. Containers
* `docker run -d --rm --name goals <image> ` : explicitly name the
* `docker run -p 3000:80 -d --rm --name goalsapp goals:latest` example

### ii. Images
* `docker build -t <name>:<tag> ` : flag:`t` for tag
* `docker build -t goals:latest .\nodejs-attached`

# II. Volumes
* `docker volume ls`


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