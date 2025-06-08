import bcrypt

def test_hash_valido():
    password = "123456"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    assert bcrypt.checkpw(password.encode(), hashed)
