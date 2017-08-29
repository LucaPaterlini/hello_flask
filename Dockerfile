FROM thebinary/alpine-flask
MAINTAINER Luca Paterlini "paterlini.luca@gmail.com"
COPY . /hello_flask
WORKDIR /hello_flask
RUN pip install -U flask-cors
ENTRYPOINT ["python"]
CMD ["hello.py"]
