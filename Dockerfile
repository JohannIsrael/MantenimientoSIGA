# docker build -t itm:sarh-app .
# pull official base image
FROM python:3.8

# set workdir directory
WORKDIR /opt/sarh/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN  apt update && apt-get install -qy \
	locales \
	locales-all \
	libpq-dev \
	python3-dev \
	musl-dev

ENV LC_ALL es_MX.UTF-8
ENV LANG es_MX.UTF-8
ENV LANGUAGE es_MX.UTF-8

# install dependencies
RUN pip install --upgrade pip

# Copiar el archivo requirements.txt en el contenedor
COPY ./app/requirements.txt /opt/sarh/app/requirements.txt
RUN pip install -r /opt/sarh/app/requirements.txt
COPY ./app /opt/sarh/app

