from app.users import users_db
import bcrypt

MAX_ATTEMPTS = 5

def verificar_credenciales(username: str, password: str) -> str:
    user = users_db.get(username)
    if not user:
        return "Usuario no encontrado"

    if user["blocked"]:
        return "Cuenta bloqueada"

    if bcrypt.checkpw(password.encode(), user["password"]):
        user["attempts"] = 0
        return "Acceso concedido"
    else:
        user["attempts"] += 1
        if user["attempts"] >= MAX_ATTEMPTS:
            user["blocked"] = True
            return "Cuenta bloqueada por exceso de intentos"
        return "Contraseña incorrecta"
