# Use the official Python 3 image.
# https://hub.docker.com/_/python
#
# python:3 builds a 954 MB image - 342.3 MB in Google Container Registry
# FROM python:3
#
# python:3-slim builds a 162 MB image - 51.6 MB in Google Container Registry
# FROM python:3-slim
#
# python:3-alpine builds a 97 MB image - 33.2 MB in Google Container Registry
FROM python:3.11-slim-buster

# RUN apt-get update -y
# RUN apt-get install -y python-pip

COPY . /www

# Create and change to the app directory.
WORKDIR /www

# RUN apt-get update && apt-get install -y --no-install-recommends

RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup.
CMD ["gunicorn", "--bind", ":80", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]