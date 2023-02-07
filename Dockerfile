FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9 as build-stage

COPY requirements.txt ./app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

COPY ./app /app

EXPOSE 8008:8008
WORKDIR /app
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload","--port","8008" ]


