FROM python:3.9-slim-buster

WORKDIR /app

COPY Requirement.txt .

RUN pip3 install --no-cache-dir -r Requirement.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
