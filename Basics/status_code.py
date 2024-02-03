################################################################################
#
# `status_code` paramter to the http operation decorator can be passed
# to indicate the what status code should the http operation send.
#
# We can also use
#
#       from fastapi import status
#       status.HTTP_201_CREATED, ...
#
#       from http import HTTPStatus
#       HTTPStatus.OK, HTTPStatus.CREATED, ...
#
################################################################################


from fastapi import FastAPI
from starlette import status


server = FastAPI()


@server.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return { "name": name }
