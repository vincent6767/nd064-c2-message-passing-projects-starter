FROM python:3.8.3-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-u", "location_consumer.py"]