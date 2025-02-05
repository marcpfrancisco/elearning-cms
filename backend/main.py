from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "0c2f06307174bc98acf1bfdfe82787ce76ed81d02d36024f417dc59474881d46"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Get
@app.get("/test/")
async def test():
  return {"Hello World"}
  

# Get /{user_id}

# Post

# PUT

# DELETE