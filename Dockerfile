FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /Docktar
# RUN apk update && apk add postgresql-dev libffi-dev gcc python3-dev musl-dev
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

