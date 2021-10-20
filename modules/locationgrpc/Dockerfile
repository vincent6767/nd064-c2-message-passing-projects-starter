FROM vincentbiasa6767/python-grpc:latest

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "-u", "location_server.py"]