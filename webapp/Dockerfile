FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

WORKDIR /app

COPY ./requirements.txt ./
COPY ./entrypoint.sh ./
COPY ./src ./src
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]




