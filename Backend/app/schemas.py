from pydantic import BaseModel
from typing import  Optional

class UserSchema(BaseModel):
    id:Optional[int] = None
    first_name: str
    last_name: str
    user_name:str
    email:str
    phone_number: str
    password:str

class DataUser(BaseModel):
    user_name:str
    password:str