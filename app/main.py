from fastapi import FastAPI
from routes.contact import router as contacts_router
from models.contacts import *


app = FastAPI()

@app.get("/")
def health():
    return {"healthy"}

app.include_router(contacts_router)
