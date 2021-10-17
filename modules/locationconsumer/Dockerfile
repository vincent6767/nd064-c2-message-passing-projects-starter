FROM python:3.7-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-u", "location_consumer.py"]