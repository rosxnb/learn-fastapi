########################################################################################
#
# Validation can be done for fields inside the request body using Field() function.
#
########################################################################################


from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated


server = FastAPI()


class Item(BaseModel):
    name: str
    description: Annotated[
        str | None,
        Field(
            title = "Description of the item",
            max_length = 1000,
        )
    ] = None
    price: Annotated[
        float,
        Field(
            gt = 0,
            description = "Price must be greater that zero",
        )
    ]
    tax: float | None = None



@server.post("/items")
async def post_item(
    item: Annotated[
        Item,
        Body( embed = True ),
    ],
) -> Item:
    return item
