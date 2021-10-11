FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache g++ gcc musl-dev linux-headers geos libc-dev postgresql-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir --force-reinstall -Iv grpcio==1.41.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "location_server.py"]