FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev 

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]