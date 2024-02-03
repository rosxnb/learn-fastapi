##############################################################################
#
# `Form()` function can be used to receive form fields instead of JSON
#
# >> pip install python-mulipart
#
##############################################################################


from fastapi import FastAPI, Form
from typing import Annotated


server = FastAPI()


@server.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return { "username": username, "password": password[-1] }
