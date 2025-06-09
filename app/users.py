import bcrypt

# Contraseña ya hasheada (plaintext: "123456")
hashed_password = bcrypt.hashpw("123456".encode(), bcrypt.gensalt())

users_db = {
    "admin": {
        "username": "admin",
        "password": hashed_password,
        "attempts": 0,
        "blocked": False
    }
}

