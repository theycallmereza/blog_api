FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev
RUN apk --update add postgresql-client
RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r /requirements.txt
RUN apk del build-deps

COPY ./docker-entrypoint.sh docker-entrypoint.sh
#RUN chmod a+x /docker-entrypoint.sh

RUN mkdir /app
WORKDIR /app
COPY ./app /app

ENTRYPOINT ["docker-entrypoint.sh"]

RUN adduser -D user
RUN chown -R user:user /docker-entrypoint.sh
RUN chmod -R 777  /docker-entrypoint.sh
USER user