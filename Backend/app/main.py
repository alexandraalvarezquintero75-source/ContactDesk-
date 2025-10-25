from fastapi import FastAPI
from app.crud import contats
from app.db import engine
from app.models import Base




app = FastAPI(
    title="ContactDesk API",
    description="API to manage contacts, users, and authentication",
    version="1.0.0"
)

app.include_router(contats)

Base.metadata.create_all(bind=engine)