##################################################################################################
#
# 1) Path parameters can be decalerd with same syntax used by Python format strings.
# 2) Order Matters for situations with fixed path (users/me) and path parameter (user/{user_id}).
#
##################################################################################################


from fastapi import FastAPI

server = FastAPI()


##################################################################################################
# Must: user_name
@server.get("/greetings/{user_name}")
async def greet_user(user_name: int) -> dict[str, str]:
    return { "message": f"Welcome, {user_name} 👻" }



##################################################################################################
# Order Matters
@server.get("/users/me")
async def get_default_user() -> str:
    return "Roshan Bharati"


@server.get("/users/{user_id}")
async def get_user_by_id(user_id: int) -> str:
    return f"User Id: {user_id}"



##################################################################################################
# predefined path parameter values

from enum import Enum


# define allowed parameter values with enum
# Inherit from str first (to tell FastAPI the type of parameter data), then Enum (to define possible values)
# Path parameters values can be str values assigned to Enum, not the enum itself
# Ex: fnn = "alexnet", then valid: models/alexnet, invalid: models/fnn
class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"
    resnet = "resnet"


@server.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, ModelName | str]:
    if model_name.value == "alexnet":
        return { "model_name": model_name, "message": "Deep Learning FTW!" }

    if model_name == ModelName.lenet:
        return { "model_name": model_name, "message": "LeCNN all the images" }

    return { "model_name": model_name, "message": "Have some resudials" }



##################################################################################################
# passing path-to-file as path parameter

# `:path` - the path converter tells FastAPI to match any path
# ex: file_path: okay/this.txt --------- files/okay/this.txt
# ex: file_path: /bin/ls -------- files//bin/ls

@server.get("/files/{file_path:path}")
async def read_file(file_path:str) ->  dict[str, str]:
    return { "file_path": file_path }

