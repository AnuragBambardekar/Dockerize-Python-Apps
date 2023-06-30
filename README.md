# Dockerization

## Steps to make a container:
```docker build -t iris-dockerization .```

```docker run -p 9999:9999 iris-dockerization```

To check, run this in CMD: <br>
```cmd
telnet 127.0.0.1 9999
```

## FastAPI - Dockerization
- to make REST API's

```cmd 
pip install fastapi uvicorn
```
```docker build -t fast-api .```

```docker run -p 8000:8000 --name mycontainername fast-api```

Go to : http://127.0.0.1:8000/

## References:

- https://www.youtube.com/watch?v=0TFWtfFY87U&t