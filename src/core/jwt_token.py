from jose import jwt
from datetime import datetime, timedelta
from pwdlib import PasswordHash 


SECRET_KEY = "cb8b3037b018196889b51bb733c28e300d76110f53bd85860a41ad627ed01908"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

def get_password_hash(password):
    return password_hash.hash(password)


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt