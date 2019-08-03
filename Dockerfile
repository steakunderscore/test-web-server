# Dockerfile

FROM python:3-slim

WORKDIR /app

ADD requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

EXPOSE 8080

CMD ["python", "app.py"]
