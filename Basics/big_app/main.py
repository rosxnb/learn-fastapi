from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

server = FastAPI(dependencies=[Depends(get_query_token)])


server.include_router(users.router)
server.include_router(items.router)
server.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@server.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
