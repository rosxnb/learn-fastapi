################################################################################
#
# - Multiple Body Parameters
# - Body() function to tell FastAPI the parameter is request body parameter
# - Require body parameter as JSON key with Body(embed=True)
#
################################################################################


from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Annotated


server = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None



@server.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[
        int,
        Path(
            title = "Id of item to update",
            ge = 0,
            le = 100,
        ),
    ],
    item: Item,
    q: Annotated[
        str | None,
        Query(
            title = "Query Parameter",
        )
    ] = None,
) -> dict[str, int | str | Item]:
    result = { "item_id": item_id }

    if q:
        result.update({ "q": q })

    if item:
        result.update({ "item": item })

    return result

#################### Response Sample Value #################################3
# v = {
#   "item_id": 10,
#   "q": "hello",
#   "item": {
#     "name": "risk",
#     "price": 1021,
#     "description": "don't have any right now",
#     "tax": 10
#   }
# }
###############################################################################



class User(BaseModel):
    username: str
    full_name: str | None = None


@server.put("/user/{user_id}")
async def update_item_with_user(
    user_id: Annotated[
        int,
        Path(
            title = "Id of item to update",
            gt = 100,
            le = 1000,
        ),
    ],
    item: Item,
    user: User,
    q: Annotated[
        str | None,
        Query(
            title = "Query Parameter",
        )
    ] = None,
) -> dict[str, int | str | Item | User]:
    result = { "user_id": user_id }

    if q:
        result.update({ "q": q })

    if item:
        result.update({ "item": item })

    if user:
        result.update({ "user": user })

    return result



@server.put("/singular")
async def post_singular_values(
    val: Annotated[
        str | list[str],
        Body(
            embed=True
        )
    ]
) -> str | list[str]:
    return val

