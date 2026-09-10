FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Koyeb передает порт через переменную PORT (по умолчанию 8000)
CMD ["python", "main.py"]
