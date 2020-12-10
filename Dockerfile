FROM python:3.7-slim-buster
EXPOSE  8000
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /code
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]