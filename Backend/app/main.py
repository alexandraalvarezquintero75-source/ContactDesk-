from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crud import contact
from app.db import engine
from app.models import Base

app = FastAPI(
    title="ContactDesk API",
    description="API to manage contacts, users, and authentication",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact)

Base.metadata.create_all(bind=engine)
