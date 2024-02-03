###############################################################
#
# We can decalre examples for a pydantic model
# which will be added to generated JSON Schema.
#
###############################################################

from fastapi import FastAPI
from pydantic import BaseModel

# from fastapi import Body
# from pydantic import Field
# from typing import Annotated

server = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None
    # price: float = Field(examples=[35.4])
    # description: str | None = Field(default=None, examples=["A very nice Item"])

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@server.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# @server.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             examples=[
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#                 {
#                     "name": "Bar",
#                     "price": "35.4",
#                 },
#                 {
#                     "name": "Baz",
#                     "price": "thirty five point four",
#                 },
#             ],
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
