FROM python:3.10-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

COPY requirements.txt ./

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate
