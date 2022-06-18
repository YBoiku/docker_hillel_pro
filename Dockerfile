FROM python:3.10-alpine

ARG WORKDIR=/wd

RUN #apt update && apt upgrade -y

WORKDIR ${WORKDIR}

COPY requirements.txt requirements.txt

RUN pip install --requirement requirements.txt

COPY ./main.py main.py
COPY ./app app

ENTRYPOINT ["python", "main.py"]