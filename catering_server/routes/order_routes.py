from fastapi import APIRouter, HTTPException, Query
from catering_server.models.admin_models import MenuItemDB
from ..models.order_models import NewOrderItem, OrderCreate, OrderDB, OrderItemDB, OrderStatusUpdate
from ..database import database
from sqlalchemy import delete, distinct, select, text, insert, update

router = APIRouter()

# Get all orders for kitchen
@router.get("/orders/kitchen")
async def get_kitchen_orders(status: str = Query(None, pattern="^(open|in_progress|ready|delivered|cancelled)$")):
    query = (
        select(OrderDB)
        .join(OrderItemDB, OrderDB.id == OrderItemDB.order_id)
        .join(MenuItemDB, OrderItemDB.menu_item_id == MenuItemDB.id)
        .where(MenuItemDB.type == "food")
    )
    if status:
        query = query.where(OrderDB.status == status)

    rows = await database.fetch_all(query)
    return {"orders": [dict(row) for row in rows]}

# Get all orders for bar
@router.get("/orders/bar")
async def get_bar_orders(status: str = Query(None, pattern="^(open|in_progress|ready|delivered|cancelled)$")):
    query = (
        select(OrderDB)
        .join(OrderItemDB, OrderDB.id == OrderItemDB.order_id)
        .join(MenuItemDB, OrderItemDB.menu_item_id == MenuItemDB.id)
        .where(MenuItemDB.type == "drink")
    )
    if status:
        query = query.where(OrderDB.status == status)

    rows = await database.fetch_all(query)
    return {"orders": [dict(row) for row in rows]}

@router.post("/orders")
async def create_order(order: OrderCreate):
    async with database.transaction():
        # Berechne total
        total = 0
        for item in order.items:
            price_query = select(MenuItemDB.price).where(MenuItemDB.id == item.menu_item_id)
            result = await database.fetch_one(price_query)
            if not result:
                raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} not found")
            total += result.price * item.quantity

    async with database.transaction():
        query_order = insert(OrderDB).values(
            table_id=order.table_id,
            status=order.status,
            created_by=order.created_by,
            total=total
        ).returning(OrderDB.id)
        order_row = await database.fetch_one(query_order)
        order_id = order_row.id

        for item in order.items:
            query_item = insert(OrderItemDB).values(
                order_id=order_id,
                menu_item_id=item.menu_item_id,
                quantity=item.quantity,
                note=item.note
            )
            await database.execute(query_item)

    return {"status": "created", "order_id": order_id,"total": float(total)}

@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    query = select(OrderDB).where(OrderDB.id == order_id)
    order = await database.fetch_one(query)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {
        "id": order.id,
        "table_id": order.table_id,
        "status": order.status,
        "created_by": order.created_by,
        "created_at": order.created_at,
        "total": float(order.total)
    }

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = delete(OrderDB).where(OrderDB.id == order_id).returning(OrderDB.id)
    row = await database.fetch_one(query)
    if not row:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"status": "deleted", "id": row.id}

# Status Update
@router.put("/orders/{order_id}")
async def update_order_status(order_id: int, data: OrderStatusUpdate):
    query = (
        update(OrderDB)
        .where(OrderDB.id == order_id)
        .values(status=data.status)
        .returning(OrderDB.id, OrderDB.status)
    )
    result = await database.fetch_one(query)

    if result:
        return {"status": "updated", "order_id": result.id, "new_status": result.status}
    else:
        raise HTTPException(status_code=404, detail="Order not found")
    
from pydantic import BaseModel

class OrderItemUpdate(BaseModel):
    quantity: int
    note: str

# Update quantity and note of Order Item
@router.put("/orders/{order_id}/items/{item_id}")
async def update_order_item(order_id: int, item_id: int, data: OrderItemUpdate):
    query = (
        update(OrderItemDB)
        .where(OrderItemDB.id == item_id)
        .values(quantity=data.quantity, note=data.note)
        .returning(OrderItemDB.id)
    )
    result = await database.fetch_one(query)

    if result:
        return {"status": "updated", "item_id": result.id}
    raise HTTPException(status_code=404, detail="Item not found")


# Add new item to an existing order
@router.post("/orders/{order_id}/items")
async def add_order_item(order_id: int, item: NewOrderItem):
    query = insert(OrderItemDB).values(
        order_id=order_id,
        menu_item_id=item.menu_item_id,
        quantity=item.quantity,
        note=item.note
    ).returning(OrderItemDB.id)

    result = await database.fetch_one(query)
    return {"status": "added", "item_id": result.id}

# Delete an item from an order
@router.delete("/orders/{order_id}/items/{item_id}")
async def delete_order_item(order_id: int, item_id: int):
    query = delete(OrderItemDB).where(
        OrderItemDB.menu_item_id == item_id
    ).returning(OrderItemDB.id)

    result = await database.fetch_one(query)
    if result:
        return {"status": "deleted", "item_id": result.id}
    raise HTTPException(status_code=404, detail="Item not found")

# Get all items of an order
@router.get("/orders/{order_id}/items")
async def get_order_items(order_id: int):
    query = select(OrderItemDB).where(OrderItemDB.order_id == order_id)
    rows = await database.fetch_all(query)
    return {
        "items": [
            {"id": r.id, "menu_item_id": r.menu_item_id, "quantity": r.quantity, "note": r.note}
            for r in rows
        ]
    }

