#FROM python:3.12-slim

#WORKDIR /app

#COPY source/requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt

#COPY source/ .

#CMD ["python", "train.py"]
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r source/requirements.txt

CMD ["python", "source/score.py"]