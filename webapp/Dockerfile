FROM python:3.9-alpine

# set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev
RUN pip install --upgrade pip

COPY ./webapp/requirements.txt ./
COPY ./webapp/entrypoint.sh ./

RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

COPY ./src ./src


ENTRYPOINT ["sh", "entrypoint.sh"]

#CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]




