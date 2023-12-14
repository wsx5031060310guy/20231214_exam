FROM python:3.9.16

WORKDIR /app

COPY ./app /app

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

RUN chmod +x fetch.py
RUN mv fetch.py fetch

