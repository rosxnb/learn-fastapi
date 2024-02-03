###################################################################################
#
# When you declare other function parameters that are not part
# of the path parameters, they are interpreted as query parameters.
#
# The query is the set of key-value pair
# that go after ? in a URL
# seperated by &
#
###################################################################################


from fastapi import FastAPI

server = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]



###################################################################################
# Query Parameters are not fixed part of the path
# So they can be optional and have default values

@server.get("/items/")
async def read_item(skip: int | None = None, limit: int = 2) -> list[dict[str, str]]:
    if skip is None: skip = 2
    return fake_items_db[skip : skip + limit]



###################################################################################
# Required Query Parameter

@server.get("/items/company")
async def get_company(needy: bool) -> str:
    return "soooonedy 👩❤️👨" if needy else "lone warrior 🫡"




###################################################################################
# Path and Query Parameter
# FastAPI can distict between path and query parameters

@server.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, q: str | None = None, short: bool = False) -> dict[str, int | str]:
    item = {
        "item_id": item_id,
        "owner_id": user_id,
    }

    if q:
        item.update({ "q" : q })

    item.update({ "description": f"This item has {'short' if short else 'long'} description" })
    return item

