# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
