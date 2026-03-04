# Partiamo da una versione leggera di Python
FROM python:3.10-slim

# Creiamo una cartella di lavoro dentro il container
WORKDIR /app

# Copiamo il nostro script dentro il container
COPY app.py .

# Comando per avviare lo script quando il container parte
CMD ["python", "app.py"]
