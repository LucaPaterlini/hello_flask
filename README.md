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