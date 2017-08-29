FROM frolvlad/alpine-python2

ADD hello.py /

RUN pip install flask

CMD [ "python", "./hello.py" ]

