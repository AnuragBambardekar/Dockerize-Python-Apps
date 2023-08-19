# Dockerization

## Why Docker?
- More than just a virtual environment
- Isolated environment for all dependencies
- Multiple services
- Easy deployment
- Same Environment for collaborators
- Play around with Python Versions for instance

## Iris Dataset - Dockerization:
```docker build -t iris-dockerization .```

```docker run -p 9999:9999 iris-dockerization```

To check, run this in CMD: <br>
```cmd
telnet 127.0.0.1 9999
```

## FastAPI - Dockerization:
- to make REST API's

```cmd 
pip install fastapi uvicorn
```
```docker build -t fastapi-image .``` - Build container image

```docker run -p 8000:8000 --name mycontainername fastapi-image``` - Run a new container

```docker start mycontainername``` - Start existing container

```docker stop mycontainername``` - Stop container

```docker rm mycontainername``` - Remove container

```docker run -p 8000:8000 --name mycontainername -d fastapi-image``` - Run container in background

```docker ps -a``` - List containers

Go to : http://127.0.0.1:8000/

**But, my code is in local system, if I make any changes it won't show up in the container.**

So, let's make a volume to persist the data.

```docker run -p 8000:8000 --name mycontainername -d -v ${pwd}:/fast-api fastapi-image``` - where /fast-api is the WORKDIR defined in the Dockerfile

```docker run -p 80:80 --name mycontainername -d -v ${pwd}:/fast-api fastapi-image``` - Docker Volumes with live reload

**Download "Dev Container" extension and Enable it in VSCode.** <br>
- Open Command Palette
- Select - "Attach to Runnning Container"
- You will get cmd console inside the Linux Container

```cmd
root@a1790f97b3e3:~# ls
root@a1790f97b3e3:~# cd ..
root@a1790f97b3e3:/# ls
bin   dev  fast-api  lib    lib64   media  opt   root  sbin  sys  usr
boot  etc  home      lib32  libx32  mnt    proc  run   srv   tmp  var
root@a1790f97b3e3:/# 
```

**Making a docker-compose.yml file**

Instead of:
```cmd
docker run -p 80:80 --name mycontainername -d -v ${pwd}:/fast-api fastapi-image
```

We can use the docker-compose.yml file, and to launch it:

```cmd
docker-compose up
```

And, to shut it down:

```cmd
docker-compose down
```

We can install additional services too, using docker-compose.yml file:

Also, remember to add it to requirements.txt if it's a python dependency.

```cmd
docker-compose up --build -d
```

**Adding DEBUGGING (debugpy)**

- Add debugpy to requirements.txt
- Set a breakpoint in main.py
- Open Run & Debug console in VSCode
- Create a launch.json file
- Run Debug and configure to localhost:5678

# Container Registries

Container registries are repositories that store and manage container images. Container images are standalone, executable software packages that include everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings.

# docker run vs docker compose

```cmd
docker run -d -p 8080:80 my-web-app
```

```yml
version: '3'
services:
  web:
    image: my-web-app
    ports:
      - "8080:80"
  database:
    image: postgres
    environment:
      POSTGRES_PASSWORD: mysecretpassword
```

You should use docker run for simple, single-container scenarios or as part of scripts and automation, while docker-compose is the preferred choice for defining and managing multi-container applications, especially during development and testing phases. Docker Compose simplifies the process of defining, configuring, and running multiple containers as a single application stack.

# Most used Options & Commands

```docker ps -a``` - lists all runnning processes
---
```docker image ls``` - lists all images
---
```docker container ls``` - lists all containers
---
```docker stop container_name/id``` - stops container
---
```docker rm container_name/id``` - deletes container
---
```docker rmi image_name``` - deletes image
---
```docker image prune -a``` - remove all unused images
---
```docker run -d ubuntu sleep 99 ``` - it runs the container in the background, detached from your current terminal session
---
```docker run --entrypoint echo ubuntu hello``` - override default entrypoint
---
```docker run --env MY_ENV=hello ubuntu printenv``` - define an environment variable
---
```docker run --init ubuntu ps``` - used to enable the "init" process as the PID 1 (the first process) inside a container. It is a recommended practice when running containers to improve process management and signal handling, especially for applications that may not handle signals and shutdown gracefully.
---
```docker run -it ubuntu``` - allow us to have an interactive session within the container
---
```docker run -d --name BambaContainer ubuntu``` - allow us to name the container
---
Specifying a network for my container - create isolated networks for our applications:

```docker network ls```

```docker network create my-network```

```docker network ls```

Create a container that detaches to it:

```docker run -d --network my-network ubuntu```

```docker ps```

```docker container inspect container_id | grep network```
---
```docker run --platform linux/arm64/v8 ubuntu dpkg --print-architecture``` - used to specify the target platform architecture and operating system when pulling or running Docker images.
---
```docker run --restart unless-stopped ubuntu``` - used to define the container's restart policy. It specifies what action Docker should take when a container exits (either voluntarily or due to an error) and determines whether the container should be automatically restarted.

always: This policy instructs Docker to always restart the container, regardless of how it exits. It's useful for services that should always be running.

on-failure: With this policy, Docker will restart the container only if it exits with a non-zero exit status (i.e., it fails). You can additionally specify the maximum number of restart attempts using the --restart-max-retries option.

unless-stopped: This policy is similar to always, but it won't restart the container if it was manually stopped by the user. It's useful for services that should run continuously but allow for manual intervention to stop them.

---
```docker run --rm --name this-one-will-be-gone ubuntu ps``` - used to automatically remove a container when it exits. This can be helpful for cleaning up containers that are only intended to run temporarily, such as during testing or one-off tasks.
---


## References:

- https://www.youtube.com/watch?v=0TFWtfFY87U&t - Containerize Python Applications with Docker <br>
- https://www.youtube.com/watch?v=0H2miBK_gAk - How to create a great dev environment with Docker <br>
