from pydantic import BaseModel
from typing import  Optional

class ContactResponse(BaseModel):
    id:Optional[int] = None
    first_name: str
    last_name: str
    email:str
    phone_number: str
    

class DataUser(BaseModel):
    user_name:str
    password:str