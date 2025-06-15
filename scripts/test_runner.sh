#!/bin/bash
echo "Iniciando pruebas y reporte de cobertura..."
pytest --cov=app --cov-report html

echo "✅ Reporte de cobertura generado en: htmlcov/index.html"
