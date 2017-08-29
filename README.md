# Hello Endpoint

Instructions

With root priviledges build and run
the image and run it

Build
```
  sudo docker build -t hello . 
```

run
```
  docker run -d -p 12345:5000 hello:latest
```

to access the endpoint:

http://127.0.0.1:12345/hello

to check the effect on the backend

```
sudo docker ps -a
```

search for the container id in the first column, than use it in the as
parameter in the following command

```
docker logs <container id>
```
