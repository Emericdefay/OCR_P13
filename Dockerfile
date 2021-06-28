# Base image
FROM python:3.8
# setup env var
ENV DockerFolder=/usr/src/app

# set working directory
WORKDIR $DockerFolder

# create folder
COPY requirements.txt ./

# set env vars python
ENV PYTHONUNBUFFERED 1
ENV PYTHINDONTWRITEBYTECODE 1

# install reqs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Port where django app run
EXPOSE 8000

COPY . $DockerFolder

# Start server
CMD docker-compose up