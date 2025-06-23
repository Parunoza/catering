from pydantic import BaseModel

# Tisch erstellen
class TableCreate(BaseModel):
    name: str

# Tisch umbenennen
class TableUpdate(BaseModel):
    name: str

# Menüeintrag erstellen
class MenuItem(BaseModel):
    name: str
    type: str  # "food" oder "drink"
