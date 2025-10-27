from fastapi import APIRouter, Response, HTTPException
from starlette.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND
from app.db import engine
from app.models import User
from app.schemas import ContactResponse, CreateContac
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
        contact_list = [dict(row._mapping) for row in result]
        return contact_list

# Obtener un contacto por ID
@contact.get("/contacts/{id_contact}", response_model=ContactResponse, tags=["Contacts"])
async def get_contact_id(id_contact: int):
    with engine.connect() as conn:
        result = conn.execute(
            select(User).where(User.__table__.c.id == id_contact)
        ).first()
        if result:
            return dict(result._mapping)
        raise HTTPException(status_code=404, detail="Contact not found")


# Crear contacto
@contact.post("/contacts/", status_code=HTTP_201_CREATED,  tags=["Contacts"])
async def post_contacts(contact_data: CreateContac):
    
    new_contact = contact_data.model_dump()
    
    with engine.connect() as conn:
        conn.execute(User.__table__.insert().values(**new_contact))
        conn.commit()
    
    return Response(status_code=HTTP_201_CREATED)

# Actualizar Contacto
@contact.put("/contacts/{id_contact}", response_model=CreateContac,  tags=["Contacts"])
def update_contacts(data_update: CreateContac, id_contact: int):
    with engine.connect() as conn:
        existing = conn.execute(User.__table__.select().where(User.__table__.c.id == id_contact)).first()
        if not existing:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

        conn.execute(
            User.__table__.update()
            .where(User.__table__.c.id == id_contact)
            .values(
                first_name=data_update.first_name,
                last_name=data_update.last_name,
                email=data_update.email,
                phone_number=data_update.phone_number
            )
        )

        conn.commit()

        result = conn.execute(User.__table__.select().where(User.__table__.c.id == id_contact)).first()
        return dict(result._mapping)


# Eliminar Contacto
@contact.delete("/contacts/{id_contact}", tags=["Contacts"])
async def delete_contacts(id_contact: int):
    with engine.connect() as conn:
        existing = conn.execute(User.__table__.select().where(User.id == id_contact)).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Contact not found")

        conn.execute(
            User.__table__.delete()
            .where(User.id == id_contact)
        )
        conn.commit()
        return Response(status_code=204)
