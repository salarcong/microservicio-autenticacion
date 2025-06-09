from fastapi import FastAPI, HTTPException
from app.auth import verificar_credenciales
from app.models import UserLogin, LoginResponse

app = FastAPI()

@app.post("/login", response_model=LoginResponse)
def login(data: UserLogin):
    resultado = verificar_credenciales(data.username, data.password)

    if resultado == "Acceso concedido":
        return {"mensaje": "Bienvenido"}
    elif "bloqueada" in resultado:
        raise HTTPException(status_code=403, detail=resultado)
    else:
        raise HTTPException(status_code=401, detail=resultado)
