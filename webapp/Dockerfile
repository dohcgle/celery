FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
COPY ./entrypoint.sh ./
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt
COPY ./src ./src

ENTRYPOINT ["sh", "entrypoint.sh"]

CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]




