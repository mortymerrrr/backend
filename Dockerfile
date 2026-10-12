FROM python:3.10-slim

WORKDIR /app

# Сначала зависимости — используем кеш слоёв
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Затем код
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
