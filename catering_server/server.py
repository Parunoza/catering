from fastapi import FastAPI
from pydantic import BaseModel
from .routes.admin_routes import router as admin_router

app = FastAPI()

app.include_router(admin_router)

class Message(BaseModel):
    text: str

@app.post("/message")
def receive_message(msg: Message):
    print(f"Nachricht erhalten: {msg.text}")
    return {"status": "ok", "echo": msg.text}

