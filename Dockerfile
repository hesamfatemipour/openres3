FROM ubuntu:20.04

ADD . /middleware

WORKDIR /middleware

RUN apt update -y && apt install build-essential python-dev python3-pip uwsgi uwsgi-python3 -y

RUN pip3 install -r ./requirements.pip

RUN chmod +x ./entrypoint

ENTRYPOINT ["/entrypoint.sh", "uwsgi"]
