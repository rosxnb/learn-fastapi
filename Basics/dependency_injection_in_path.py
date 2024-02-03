#############################################################
# 
# In some cases you don't really need the return value of a dependency inside your path operation function.
# Or the dependency doesn't return a value.
# But you still need it to be executed/solved.
# For those cases, instead of declaring a path operation function parameter with Depends, 
# you can add a list of dependencies to the path operation decorator.
#
#############################################################


from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated

server = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@server.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
