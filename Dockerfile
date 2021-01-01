FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
RUN apt update -y && apt install build-essential python-dev python3-pip uwsgi tzdata -y

COPY ./requirements.pip ./requirements.pip

ADD . /openres3
WORKDIR /openres3

RUN pip3 install -r requirements.pip

copy . /openres3

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh", "uwsgi"]
