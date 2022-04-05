FROM python:3.8.10
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/mainapp
COPY requirements.txt ./
RUN pip install -r requirements.txt