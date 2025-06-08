from app.auth import verificar_credenciales
from app.users import users_db

def test_login_correcto():
    resultado = verificar_credenciales("admin", "123456")
    assert resultado == "Acceso concedido"

def test_login_incorrecto():
    resultado = verificar_credenciales("admin", "badpass")
    assert resultado == "Contraseña incorrecta"

def test_bloqueo_por_intentos():
    users_db["admin"]["attempts"] = 4
    resultado = verificar_credenciales("admin", "badpass")
    assert resultado == "Cuenta bloqueada por exceso de intentos"
