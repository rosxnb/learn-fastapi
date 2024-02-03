#####################################################
#
# A middleware is a function that runs for all path operations:
#   - before a request is processed by path operations
#   - before the response is sent to client
#
#####################################################


import time
from fastapi import FastAPI, Request


server = FastAPI()


@server.middleware("http")
async def add_preocess_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
