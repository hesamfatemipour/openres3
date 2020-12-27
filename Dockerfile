FROM ubuntu:20.04

ADD . /middleware

WORKDIR /middleware

RUN apt update -y && apt install python3-pip -y

RUN pip3 install -r ./requirements.pip

CMD [ "python3", "./middleware/middleware.py"]