from fastapi import APIRouter, HTTPException
from ..models.admin_models import TableCreate, TableUpdate, MenuItem
from ..data.storage import tables, menu_items

router = APIRouter()

# Tische

@router.post("/admin/table")
def add_table(table: TableCreate):
    table_id = len(tables) + 1
    tables.append({"id": table_id, "name": table.name})
    return {"status": "ok", "added": {"id": table_id, "name": table.name}, "all_tables": tables}

@router.get("/admin/tables")
def get_tables():
    return {"tables": tables}

@router.put("/admin/table/{table_id}")
def update_table(table_id: int, new_data: TableUpdate):
    for table in tables:
        if table["id"] == table_id:
            table["name"] = new_data.name
            return {"status": "updated", "table": table}
    raise HTTPException(status_code=404, detail="Table not found")

@router.delete("/admin/table/{table_id}")
def delete_table(table_id: int):
    for i, table in enumerate(tables):
        if table["id"] == table_id:
            deleted = tables.pop(i)
            return {"status": "deleted", "table": deleted, "remaining": tables}
    raise HTTPException(status_code=404, detail="Table not found")

# Menü

@router.get("/admin/menu")
def get_menu():
    return {"menu": menu_items}

@router.post("/admin/menu")
def add_menu_item(item: MenuItem):
    item_id = len(menu_items) + 1
    menu_items.append({"id": item_id, "name": item.name, "type": item.type})
    return {"status": "added", "item": {"id": item_id, "name": item.name, "type": item.type}}

@router.delete("/admin/menu/{item_id}")
def delete_menu_item(item_id: int):
    for i, item in enumerate(menu_items):
        if item["id"] == item_id:
            deleted = menu_items.pop(i)
            return {"status": "deleted", "item": deleted}
    raise HTTPException(status_code=404, detail="Menu item not found")
