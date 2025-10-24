from fastapi import APIRouter,Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from app.db import engine
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()

# Ruta de prueba
@user.get("/")
async def root():
    return{
        'message': 'hi, i am a developer'
    }


