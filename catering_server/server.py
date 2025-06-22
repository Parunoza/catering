from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/message")
def receive_message(msg: Message):
    print(f"Nachricht erhalten: {msg.text}")
    return {"status": "ok", "echo": msg.text}
