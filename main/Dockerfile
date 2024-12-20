FROM python:3-alpine

WORKDIR /docker-website
COPY . .

RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]