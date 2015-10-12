FROM grahamdumpleton/mod-wsgi-docker:python-3.4-onbuild

RUN apt-get update
RUN apt-get install -y python3.4

RUN apt-get update
RUN apt-get install -y python3.4-dev

RUN apt-get install -y \
    python3-pip \
    python-setuptools

RUN pip3 install -Iv Flask==0.10.1 \
    requests

EXPOSE 80

ADD . /app

CMD [ "hyperion.wsgi" ]