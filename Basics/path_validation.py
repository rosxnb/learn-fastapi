###############################################################################
#
# Path validation can be performed in the same way as the Query Validation.
# For query validation we used Query() function.
# For path validation we shall use Path() function 😉.
#
###############################################################################


from fastapi import FastAPI, Path, Query
from typing import Annotated


server = FastAPI()


@server.get("/items/{item_id}")
async def get_item_by_id(
    item_id: Annotated[
        int, 
        Path(
            title = "The ID of the item to get",
            ge = 4,
            le = 6,
            # gt = 4,
            # lt = 6,
        ),
    ],
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
        ),
    ] = None
) -> dict[str, int | str]:

    results = { "item_id": item_id }
    if q:
        results.update({ "q": q })

    return results
