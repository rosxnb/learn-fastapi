#####################################################################
#
# FastAPI allows us to declare additional information and validation
# for the query parameters.
#
#####################################################################


from fastapi import FastAPI

server = FastAPI()


# FastAPI will know "q" is not required since it has default value
@server.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



#####################################################################
# Though optional, "q" can have constraints like max-length

from typing import Annotated
from fastapi import Query


@server.get("/constraints/items/")
async def constrained_items(
    q: Annotated[
        str | None, 
        Query(
            min_length=5, 
            max_length = 50, 
            pattern = "^unmodifiable$")
    ] = None ):

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results



#####################################################################
# Query Parameter List / Multiple Values
# "/?q=hello&q=world"
# { "q": ["hello", "world"] }

# alias for query parameter to be used in python
# title and description for better documentation
# deprecate query parameter
# exclude query parameter from API schema

@server.get("/multiple/items/")
async def get_multiple_items(
    aliased_query: Annotated[
        list[str], 
        Query(
            alias="item-query",
            min_length = 1,
            title = "Required query parameter",
            description="Not optional since it does not have a default value. Use 'item-query' not 'q'.",
            deprecated=True,
        ),
    ],
    q: Annotated[
        str | None,
        Query(
            include_in_schema=False
        )
    ] = None ):

    aliased_query = { "q": aliased_query }
    if q:
        aliased_query.update({ "junk": q })
    return aliased_query
