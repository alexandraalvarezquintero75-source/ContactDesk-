from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from app.db import engine
from app.models import User
from app.schemas import ContactResponse, DataUser
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from sqlalchemy import select

contats = APIRouter()

# Ruta de prueba
@contats.get("/")
async def root():
    return {
        "message": "hi, i am a developer"
    }

# Obtener todos los contactos
@contats.get("/contacts", response_model=List[ContactResponse], tags=["Contacts"])
async def get_contacts():
    with engine.connect() as conn:
        # 🔧 Corregido: se usa __table__ en lugar de __tablename__
        result = conn.execute(User.__table__.select()).fetchall()
        user_list = [dict(row._mapping) for row in result]
        return user_list

# Obtener un contacto por ID
@contats.get("/contacts/{id_contact}", response_model=ContactResponse, tags=["Contacts"])
async def get_contact_id(id_contact: int):
    with engine.connect() as conn:
        result = conn.execute(
            select(User).where(User.id == id_contact)
        ).first()
        if result:
            return dict(result._mapping)
        return {"error": "Contact not found"}
