FROM python:3.12-alpine

COPY ./scripts /
COPY ./app /app
WORKDIR /app/

RUN apk add --no-cache bash; pip install pip -r /app/requirements.txt --upgrade; chmod +x /*.sh

ENV PYTHONPATH=/app \
    MODULE_NAME=whoami \
    VARIABLE_NAME=app

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/run.sh"]
