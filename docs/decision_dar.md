# Decisión Técnica – Semana 8
**Área de proceso:** Decision Analysis and Resolution (DAR)  
**Proyecto:** Microservicio de Autenticación Segura  
**Tema:** Elección entre JWT y OAuth2

---

# Alternativas evaluadas

| Alternativa | Descripción breve |
|-------------|-------------------|
| JWT         | Token firmado localmente que contiene datos del usuario. Se verifica sin servidor externo. |
| OAuth2      | Protocolo completo de autorización. Requiere servicios externos (como Google, Azure AD). |

---

# Criterios de evaluación

| Criterio                | Peso  |
|-------------------------|-------|
| Seguridad               | 50%   |
| Facilidad de integración| 30%   |
| Documentación y soporte | 20%   |

---

# Evaluación técnica (ponderada)

```python
# decision_eval.py
criterios = ["seguridad", "implementacion", "soporte"]
pesos = [0.5, 0.3, 0.2]

opciones = {
    "JWT":    [8, 9, 9],
    "OAuth2": [9, 5, 8]
}

def evaluar(opcion):
    return sum(p * w for p, w in zip(opciones[opcion], pesos))

print("Puntajes:")
for nombre in opciones:
    print(f"{nombre}: {evaluar(nombre):.2f}")
