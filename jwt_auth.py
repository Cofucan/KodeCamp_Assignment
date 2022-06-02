from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from jose import jwt

app = FastAPI()

SECRET_KEY = "f838b8dab4c6b188ad57105879f77d06e35a4b5905deaba44b2bf313121c1b7c"
ALGORITHM = "HS256"


# ACCESS_TOKEN_EXPIRE_MINUTES = 1440     # Expires in 24 hours


class Token(BaseModel):
    username: str
    email: EmailStr


def create_jwt(data: Token):
    data_dict = data.dict()
    encoded_jwt = jwt.encode(data_dict, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt(token):
    payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
    return payload


@app.post("/encode/")
async def create_token(data: Token):
    token_data = Token(email=data.email, username=data.username)
    token = create_jwt(data=token_data)
    return {"token": token}


@app.post("/decode/")
async def decode_token(token: str):
    payload = decode_jwt(token)
    return {"payload": payload}
