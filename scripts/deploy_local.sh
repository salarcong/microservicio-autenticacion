#!/bin/bash
echo "Activando entorno virtual..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Iniciando microservicio..."
uvicorn app.main:app --reload
