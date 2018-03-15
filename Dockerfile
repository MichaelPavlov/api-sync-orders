FROM python:3.6

ENV PYTHONUNBUFFERED 1
ADD config/requirements.txt /app/requirements.txt
WORKDIR /app
COPY src /app
RUN pip install -r requirements.txt && \
    adduser --disabled-password --gecos '' user && \
    chown -R user:user /app/* && \
    chmod -R 777 /app

USER user
