import bcrypt

def test_bcrypt_hash_and_check():
    password = "miclave123"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    assert hashed != password.encode()

    assert bcrypt.checkpw(password.encode(), hashed)

    assert not bcrypt.checkpw("clavefalsa".encode(), hashed)
