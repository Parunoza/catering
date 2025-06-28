from fastapi import FastAPI
from .routes.admin_routes import router as admin_router
from .database import database
from .routes.order_routes import router as order_router

app = FastAPI()

app.include_router(admin_router)
app.include_router(order_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



