FROM python:3.9

COPY ./alembic /alembic
COPY alembic.ini /

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

RUN chmod +x init.sh

CMD ["./init.sh"]
