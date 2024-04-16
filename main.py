from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from routes.usersRoute import userRoutes
from routes.defaultRoute import defaultRoute

app = FastAPI(title="FastAPI-Users-Backend", description="CRUD API")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(userRoutes, tags=['Users'], prefix='/api')
app.include_router(defaultRoute)
