# Base image
FROM python:3.8

# setup env vars
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /django

# create folder
COPY requirements.txt requirements.txt

# install reqs
RUN pip3 install -r requirements.txt

# Allow port 8000
EXPOSE 8000

# Run server localy
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]