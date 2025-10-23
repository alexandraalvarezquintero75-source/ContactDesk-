from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import declarative_base
from db import engine

Base = declarative_base()
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    password = Column(String(255), nullable=False)