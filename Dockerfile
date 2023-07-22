ARG VERSION=0.1

FROM python:3.10-alpine
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app
VOLUME /app/templates

EXPOSE 80
CMD ["gunicorn", "--chdir", "/app", "app:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:80"]
