# Instructions to run to Push to GitHub:
```cmd
docker login --username AnuragBambardekar --password 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 ghcr.io  
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
