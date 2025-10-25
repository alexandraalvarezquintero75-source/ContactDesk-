from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import re

class ContactResponse(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    phone_number: str
    

class DataUser(BaseModel):
    user_name: str
    password: str


class CreateContac(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

    # Validar que first_name solo tenga letras
    @field_validator("first_name")
    def first_name_letters_only(cls, v):
        if not v.isalpha():
            raise ValueError("El nombre solo puede contener letras")
        return v

    # Validar que last_name solo tenga letras
    @field_validator("last_name")
    def last_name_letters_only(cls, v):
        if not v.isalpha():
            raise ValueError("El apellido solo puede contener letras")
        return v

    # Validar que phone_number solo tenga dígitos
    @field_validator("phone_number")
    def phone_numbers_only(cls, v):
        if not re.fullmatch(r"\d+", v):
            raise ValueError("El número de teléfono solo puede contener dígitos")
        return v
