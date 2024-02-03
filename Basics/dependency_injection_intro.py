from fastapi import FastAPI, Depends
from typing import Annotated


server = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]




################ Function as Dependency #############################
async def common_params(
    q: str | None = None,
    skip: int = 0,
    limit: int = 100
):
    return { "q":q, "skip": skip, "limit": limit }

CommonParam = Annotated[dict, Depends(common_params)]




################## Class as Dependency ###############################
# This provides better editor hints
# FastAPI returns instance of class through which variables can be accessed
class CommonQueryParams:
    def __init__(
        self,
        q: str | None = None,
        skip: int = 0,
        limit: int = 100
    ):
        self.q = q
        self.skip = skip
        self.limit = limit

CommonQueryParamsClass = Annotated[CommonQueryParams, Depends()]



@server.get("/items")
async def read_items(commons: CommonQueryParamsClass):
    response = {}

    if commons.q:
        response.update({ "q": commons.q })

    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({ "items": items })
    return response
