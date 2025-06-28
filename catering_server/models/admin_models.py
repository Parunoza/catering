from pydantic import BaseModel
from decimal import Decimal
from sqlalchemy import Column, Integer, Numeric, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class RestaurantTableDB(Base):
    __tablename__ = "restaurant_table"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class TableCreate(BaseModel):
    name: str

class TableUpdate(BaseModel):
    name: str

class MenuItem(BaseModel):
    name: str
    type: str

class MenuItemCreate(BaseModel):
    name: str
    type: str
    price: Decimal

class MenuItemDB(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(
        String,
        nullable=False
    )
    price = Column(Numeric(6, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("type IN ('drink', 'food')", name="check_menu_item_type"),
    )

    from pydantic import BaseModel
from decimal import Decimal


