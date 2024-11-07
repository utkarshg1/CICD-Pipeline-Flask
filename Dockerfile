FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r --no-chache-dir requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]