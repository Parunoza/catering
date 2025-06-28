from fastapi import APIRouter, HTTPException
from ..models.admin_models import MenuItemCreate, TableCreate, TableUpdate, MenuItem, RestaurantTableDB, MenuItemDB
from ..database import database
from sqlalchemy import insert, select, update, delete, text

router = APIRouter()

# --- Tische ---

@router.post("/admin/restaurant_tables")
async def add_restaurant_table(table: TableCreate):
    query = insert(RestaurantTableDB).values(name=table.name).returning(RestaurantTableDB.id)
    row = await database.fetch_one(query)
    return {"status": "ok", "added": {"id": row.id, "name": table.name}}

@router.get("/admin/restaurant_tables")
async def get_restaurant_tables():
    query = select(RestaurantTableDB)
    rows = await database.fetch_all(query)
    return {"restaurant_tables": [{"id": row.id, "name": row.name} for row in rows]}

@router.put("/admin/restaurant_tables/{table_id}")
async def update_restaurant_table(table_id: int, new_data: TableUpdate):
    query = (
        update(RestaurantTableDB)
        .where(RestaurantTableDB.id == table_id)
        .values(name=new_data.name)
        .returning(RestaurantTableDB.id)
    )
    row = await database.fetch_one(query)
    if row:
        return {"status": "updated", "table": {"id": table_id, "name": new_data.name}}
    raise HTTPException(status_code=404, detail="Table not found")

@router.delete("/admin/restaurant_tables/{table_id}")
async def delete_restaurant_table(table_id: int):
    query = delete(RestaurantTableDB).where(RestaurantTableDB.id == table_id).returning(RestaurantTableDB.id)
    row = await database.fetch_one(query)
    if row:
        return {"status": "deleted", "id": table_id}
    raise HTTPException(status_code=404, detail="Table not found")

# --- Menü ---
@router.get("/admin/menu")
async def get_menu():
    query = select(MenuItemDB)
    rows = await database.fetch_all(query)
    return {"menu": [{"id": row.id, "name": row.name, "type": row.type, "price": row.price} for row in rows]}

@router.post("/admin/menu")
async def add_menu_item(item: MenuItemCreate):
    query = insert(MenuItemDB).values(name=item.name, type=item.type, price=item.price).returning(MenuItemDB.id)
    row = await database.fetch_one(query)
    return {"status": "added", "item": {"id": row.id, "name": item.name, "type": item.type,  "price": row.price}}

@router.delete("/admin/menu/{item_id}")
async def delete_menu_item(item_id: int):
    query = delete(MenuItemDB).where(MenuItemDB.id == item_id).returning(MenuItemDB.id)
    row = await database.fetch_one(query)
    if row:
        return {"status": "deleted", "id": item_id}
    raise HTTPException(status_code=404, detail="Menu item not found")