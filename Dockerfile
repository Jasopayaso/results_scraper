#Runnable python image
FROM python:3.10.5-alpine3.16

RUN adduser --disabled-password --uid 2461 python && mkdir /app && chown -R python:python /app

WORKDIR /app

COPY  --chown=python:python requirements.txt .
COPY --chown=python:python . app

RUN pip install -r requirements.txt --no-cache-dir

USER 2461

CMD [ "python", "app/main.py" ]