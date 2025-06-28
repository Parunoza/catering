from typing_extensions import Literal
from pydantic import BaseModel, Field, constr
from typing import List, Optional
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, TIMESTAMP, Text, CheckConstraint, func
from sqlalchemy.orm import relationship
from ..database import Base

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int
    note: Optional[str] = None


class OrderCreate(BaseModel):
    table_id: int
    status: str = Field(..., pattern="^(open|in_progress|ready|delivered|cancelled)$")
    created_by: int
    items: List[OrderItemCreate]

class OrderDB(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey("restaurant_tables.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(20), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    total = Column(Numeric(8, 2)) 
    
class OrderItemDB(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    note = Column(Text)
    
class OrderStatusUpdate(BaseModel):
    status: Literal["open", "in_progress", "ready", "delivered", "cancelled"]

class NewOrderItem(BaseModel):
    menu_item_id: int
    quantity: int
    note: str = ""

class OrderItemUpdate(BaseModel):
    quantity: int
    note: Optional[str] = ""

class NewOrderItem(BaseModel):
    menu_item_id: int
    quantity: int
    note: Optional[str] = ""

class OrderStatusUpdate(BaseModel):
    status: constr(pattern="^(open|in_progress|ready|delivered|cancelled)$")

class OrderItemUpdate(BaseModel):
    quantity: int | None = None
    note: str | None = None
