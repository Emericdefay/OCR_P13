# Base image
FROM python:3.8
# setup env var
ENV DockerFolder=/home/app/oc-lettings-site

# create folder
RUN mkdir -p $DockerFolder

# set working directory
WORKDIR $DockerFolder

# set env vars python
ENV PYTHONUNBUFFERED 1
ENV PYTHINDONTWRITEBYTECODE 1

# install reqs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Port where django app run
EXPOSE 8000

# Start server
CMD python manage.py runserver 8000