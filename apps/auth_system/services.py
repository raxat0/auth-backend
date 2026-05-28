import hashlib
import jwt

from datetime import datetime, timedelta

SECRET_KEY = 'SECRET_KEY'


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def check_password(password, hashed):
    return hashlib.sha256(
        password.encode()
    ).hexdigest() == hashed


def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )

    return token


def decode_token(token):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=['HS256']
    )