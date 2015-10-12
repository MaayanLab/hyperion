FROM debian:stable

RUN apt-get update \
    apt-get -y install vim

RUN apt-get -y install python \
    apt-get -y install python-dev \
    apt-get -y install python-pip \
    apt-get -y install python-setuptools

RUN apt-get -y install apache2 \
    apt-get -y install apache2-prefork-dev \
    pip install mod_wsgi \
    pip install -Iv Flask==0.10.1

EXPOSE 80

ADD . /hyperion

CMD /hyperion/boot.sh
