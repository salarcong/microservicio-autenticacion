from datetime import datetime

# Simulación de KPIs por sprint
kpis = [
    {"sprint": 1, "cobertura": 85, "bugs": 3, "tiempo_entrega_dias": 6},
    {"sprint": 2, "cobertura": 90, "bugs": 1, "tiempo_entrega_dias": 5},
]

for kpi in kpis:
    print(f"[Sprint {kpi['sprint']}] Cobertura: {kpi['cobertura']}% | Bugs: {kpi['bugs']} | Entrega: {kpi['tiempo_entrega_dias']} días")
