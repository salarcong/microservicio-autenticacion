from fastapi import FastAPI, HTTPException, Depends
from app.auth import verificar_credenciales
from app.models import UserLogin, LoginResponse
from app.jwt_manager import crear_token, verificar_token

app = FastAPI()

@app.post("/login")
def login(data: UserLogin):
    resultado = verificar_credenciales(data.username, data.password)

    if resultado == "Acceso concedido":
        token = crear_token({"sub": data.username})
        return {"mensaje": "Bienvenido", "token": token}
    elif "bloqueada" in resultado:
        raise HTTPException(status_code=403, detail=resultado)
    else:
        raise HTTPException(status_code=401, detail=resultado)

@app.get("/protegido")
def protegido(token: str):
    datos = verificar_token(token)
    if datos is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"usuario": datos["sub"], "mensaje": "Acceso autorizado"}
