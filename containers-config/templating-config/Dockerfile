FROM python:3.13-rc-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /app/logs


CMD [ "python3", "request_clients.py" ]

