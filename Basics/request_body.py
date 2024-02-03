##################################################################################
#
# Data is sent from client to API as a request body.
# Data is sent from API to client as a response body.
#
##################################################################################


from fastapi import FastAPI
server = FastAPI()


# To declare a request body, use Pydantic models with all their power and benefits
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@server.post("/items/")
async def create_item(item: Item) -> Item:
    item.price = item.price * 1.10 # increme by 10%
    return item


###########################################################################################
# The function parameters will be recognized as follows:

#   - If the parameter is also declared in the path, it will be used as a path parameter.
#   - If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
#   - If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
###########################################################################################
