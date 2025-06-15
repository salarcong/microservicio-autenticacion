#!/bin/bash
echo "Ejecutando análisis de seguridad y verificación de políticas..."

# Validar que el archivo .env esté en .gitignore
if grep -q ".env" .gitignore; then
    echo ".env correctamente ignorado ✅"
else
    echo "⚠️ Falta agregar .env a .gitignore"
fi

# Ejecutar análisis con Bandit
echo "Ejecutando Bandit para seguridad del código..."
bandit -r app/
