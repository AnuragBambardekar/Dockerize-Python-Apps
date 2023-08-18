# Instructions to run to Push to GitHub:
```cmd
docker login --username AnuragBambardekar --password PAT ghcr.io  
```

```cmd
docker build . -t ghcr.io/anuragbambardekar/hello-world-ghcr:latest
```
```cmd
docker push ghcr.io/anuragbambardekar/hello-world-ghcr:latest
```
```cmd
docker image ls | grep anuragbambardekar
```
```cmd
docker image rm 98979482c721 --force
```
```cmd
docker image ls | grep anuragbambardekar
```
```cmd
docker run ghcr.io/anuragbambardekar/hello-world-ghcr:latest
```

# Automatically update image on GitHub Registry

Go to the GitHub Repository's (where you have the Dockerfile) Settings

```
/Dockerize-Python-Apps/settings/secrets/actions/new
```

Create a new 'Repository Secret' and add the PAT.

Create a .github/workflows folder in root.

Also move the Dockerfile to root.

Then create a .yaml file with necessary details.
