FROM python:3.7-slim

WORKDIR /usr/src/spidy/backend

RUN apt-get upgrade && pip install --upgrade pip 

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["/bin/sh"]
