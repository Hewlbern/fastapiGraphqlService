FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements-test.txt ./app/requirements-test.txt
COPY test_main.py ./app/test_main.py


RUN pip install --no-cache-dir --upgrade -r ./app/requirements-test.txt

COPY ./app /app

WORKDIR /app


