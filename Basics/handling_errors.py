##################################################################
#
# To return Http responses with errors to the clients
# we can use `HTTPException` class.
#
# HTTPException class extends python exception
# so the code following it won't run.
#
# `detail` parameter of HTTPException converts value: list, dict, etc
# to JSON, courtesy of FastAPI.
#
##################################################################

from fastapi import FastAPI, HTTPException

server = FastAPI()

items = { "foo": "The Foo Wrestlers" }


@server.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            headers={ "X-Error": "Can also include header info" },
        )

    return { "item": items[item_id] }





####################################################################
# Custom Exception

from fastapi import Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@server.exception_handler(UnicornException)
async def unicorn_exception_handler(_: Request, ex: UnicornException):
    return JSONResponse(
        status_code = 418,
        content = {
            "message": f"Oops! {ex.name} did something. There goes a rainbow..."
        }
    )


@server.get("/unicorn/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)

    return { "unicorn_name": name }
