FROM python:3.11-slim

LABEL authors="vladimir"

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .