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



## References:

- https://www.youtube.com/watch?v=0TFWtfFY87U&t - Containerize Python Applications with Docker <br>
- https://www.youtube.com/watch?v=0H2miBK_gAk - How to create a great dev environment with Docker <br>
