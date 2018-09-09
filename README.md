
Prerequisite-

1) python3 

sudo yum install python3

# Create a virtualenv to isolate our package dependencies locally
virtualenv env

# Install Django and Django REST framework into the virtualenv
sudo pip3 install django
sudo pip3 install djangorestframework
sudo pip3 install coreapi


Step 1 - git pull code 

git clone https://github.com/srshg/Git_projects.git 

step2 - then go to directory where manage.py resides.

python3 manage.py runserver

step3 - open browser and add to run locally

http://127.0.0.1:8000/



Use Docker/docker-compose to pack up and run your apps :-

Pack and run inside docker on local Mac :-

Install docker on system 

https://www.docker.com/products/

Create directory 

ex - mkdir -p /Users/goachers/repos/django-docker

1 Create DockerFile and add this :-

FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip3 install -r requirements.txt

ADD . /code/

2. add requiremnts  

touch requirements.txt

then add

django
djangorestframework
coreapi


3. touch docker-compose.yml


then add 

version: '3.3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db


4. start sample application with same name 

docker-compose run web django-admin.py startproject CarRental_api

5. Copy project folder to overide CarRental_api folder there 

 cp -r ~/git_projects/CarRental_api/ /Users/goachers/repos/django-docker/CarRental_api

6. then run docker 

 docker-compose up

7. open browser and add to run

http://0.0.0.0:8000/
