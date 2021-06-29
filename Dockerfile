# Base image
FROM python:3.8

# setup env vars
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /django

# copy into folder /django/
COPY . /django/

# install reqs
RUN pip3 install -r requirements.txt

# Allow port
# EXPOSE $PORT

# Run server localy
CMD /bin/bash -c 'python manage.py runserver 0.0.0.0:${PORT}'