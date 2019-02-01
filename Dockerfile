FROM python:3

RUN apt-get update -q && \
apt-get install -yq genisoimage && \
apt-get autoclean -yq && \
apt-get clean -yq

WORKDIR /app

ADD requirements.txt /app/

RUN pip3 install --no-cache-dir -r /app/requirements.txt

ADD . .

ENV PORT=8080

CMD python app.py
