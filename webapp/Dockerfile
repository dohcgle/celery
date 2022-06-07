FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY ./src ./src


ENTRYPOINT ["sh", "entrypoint.sh"]




