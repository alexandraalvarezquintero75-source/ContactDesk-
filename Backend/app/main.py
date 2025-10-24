from fastapi import FastAPI
from app.crud import user


app = FastAPI()

app.include_router(user)

