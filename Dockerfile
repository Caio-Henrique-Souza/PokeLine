FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema para o Postgres se necessário
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# O container apenas disponibiliza o código; o Airflow o chamará