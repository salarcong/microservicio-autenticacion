from fastapi import FastAPI, HTTPException
from app.auth import verificar_credenciales

app = FastAPI()

@app.post("/login")
def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="Faltan datos")

    resultado = verificar_credenciales(username, password)
    
    if resultado == "Acceso concedido":
        return {"mensaje": "Bienvenido"}
    elif "bloqueada" in resultado:
        raise HTTPException(status_code=403, detail=resultado)
    else:
        raise HTTPException(status_code=401, detail=resultado)
