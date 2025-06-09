from app.jwt_manager import crear_token, verificar_token

def test_crear_y_verificar_token():
    data = {"sub": "admin"}
    token = crear_token(data)
    assert isinstance(token, str)

    payload = verificar_token(token)
    assert payload is not None
    assert payload["sub"] == "admin"

def test_token_invalido():
    token = "token.falso.noesvalido"
    assert verificar_token(token) is None
