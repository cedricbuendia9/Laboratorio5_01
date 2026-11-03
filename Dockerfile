FROM python:3.12-slim

WORKDIR /app

COPY source/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY source/ .

CMD ["python", "main.py"]