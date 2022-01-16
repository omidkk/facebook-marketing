# Python-Basisimage
FROM python:3.8.12


# Bash-Shell nutzen
SHELL ["/bin/bash", "-c"]

# Instal pip
RUN apt-get update -y
RUN apt-get -y install python3-pip


RUN mkdir /usr/local/ounass
WORKDIR /usr/local/ounass
COPY . .

RUN mkdir -p .temp/shapefile

# Installation der erforderlichen Python-Pakete
RUN pip install --upgrade pip
RUN pip install pipenv

RUN python --version

RUN pip install -r ./requirements.txt

EXPOSE 5000