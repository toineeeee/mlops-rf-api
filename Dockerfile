FROM python:3.10-slim

WORKDIR /app

COPY . /app
COPY rf_api/model /app/model

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
