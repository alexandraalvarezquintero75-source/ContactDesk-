from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from app.db import engine
from app.models import User
from app.schemas import ContactResponse, CreateContac
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from sqlalchemy import select

contact = APIRouter()

# Ruta de prueba
@contact.get("/")
async def root():
    return {
        "message": "hi, i am a developer"
    }

# Obtener todos los contactos
@contact.get("/contacts", response_model=List[ContactResponse], tags=["Contacts"])
async def get_contacts():
    with engine.connect() as conn:
    
        result = conn.execute(User.__table__.select()).fetchall()
        user_list = [dict(row._mapping) for row in result]
        return user_list

# Obtener un contacto por ID
@contact.get("/contacts/{id_contact}", response_model=ContactResponse, tags=["Contacts"])
async def get_contact_id(id_contact: int):
    with engine.connect() as conn:
        result = conn.execute(
            select(User).where(User.id == id_contact)
        ).first()
        if result:
            return dict(result._mapping)
        return {"error": "Contact not found"}

# Crear contacto
@contact.post("/contacts/", status_code=HTTP_201_CREATED,  tags=["Contacts"])
async def post_contacts(contact_data: CreateContac):
    
    new_contact = contact_data.model_dump()
    
    with engine.connect() as conn:
        conn.execute(User.__table__.insert().values(**new_contact))
        conn.commit()
    
    return Response(status_code=HTTP_201_CREATED)