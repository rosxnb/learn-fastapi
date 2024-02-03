################################################################################
#
# `response_model` parameter to http decorators of FastAPI
# can be specified to tell FastAPI the intended return type
# of a http operation.
#
# Adding a return type to http operation provides:
#   - Data Validation
#   - Data Filtering
#   - Details Schema Documentation
#   - Improved Security
#
#
# This file contains:
#   - using `response_model` parameter of decorator
#   - disabling `response_model` parameter
#   - setting default repose values
#   - not sending unset values with defaults
#   - Bool parameters: `response_model_exclude_unset`, `response_model_exclude_defaults`,  `response_model_exclude_none`
#   - Set(str) parameters: `response_model_include`, `response_model_exclude`
#
#
# >> pip install email-validator # for email body field
#
################################################################################


from typing import Any

from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse

server = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None




# This is also valid
# @server.post("/user/")
# async def create_user(user: UserIn) -> UserOut:
#     return user


@server.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user



##########################################################################################
# Turn of response_model to prevent FastAPI perform data validation and all
# With response_model turned on, FastAPI would throw error in following http operation

@server.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    return {"message": "Here's your interdimensional portal."}




###########################################################################################
# Default response model values
# use `response_model_exclude_unset` parameter to toggle sending default variable values

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@server.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]



###########################################################################################
# Default response model values
# use `response_model_include` parameter to only include certain attributes to return

@server.get("/default-items/{item_id}", response_model=Item, response_model_include=set(["name", "description"]))
async def read_item(item_id: str):
    return items[item_id]

