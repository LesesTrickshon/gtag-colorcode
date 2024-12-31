# Betriebssystem, Programmiersprache, usw
FROM python:latest

# Wo sollen die Datein gespeicher werden
WORKDIR /app

# Python-Datei in den /app ordner kopieren
COPY colorcode.py ./

# Startbefehl für die App
CMD ["python", "colorcode.py"]