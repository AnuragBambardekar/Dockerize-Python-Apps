FROM python:3.10

WORKDIR /fast-api

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python","./src/main.py"]