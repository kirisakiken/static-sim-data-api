from fastapi import FastAPI

from src.routes import world_route

app = FastAPI()
app.include_router(world_route.router)
