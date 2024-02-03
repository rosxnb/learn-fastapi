FastAPI generates a "schema" with all our API using the [OpenAPI](https://github.com/OAI/OpenAPI-Specification) standard.
> Schema definition includes the API paths, possible parameters they take, etc.
> Data schema refers to the shape of data, like a JSON content where the it would mean the JSON attributes, and data types, etc.


OpenAPI defines an API schema for our API which includes definitions of the data sent and received. JSON Schema is used as the standard for JSON data schemas.


## Default Endpoints Provided

- **Swagger Documentation**: [doc](http://localhost:8000/docs)
- **Alternative Documentation**: [redoc](http://localhost:8000/redoc)
- **JSON Data Schema**: [openapi.json](http://localhost:8000/openapi.json)


## Inheritance

**FastAPI** class inherits from [Starlette](https://www.starlette.io).


## Simple FastAPI App

```python
from fastapi import FastAPI

sever = FastAPI()

@app.get("/")
async def root():
    return { "message": "FastAPI is AMAZING!" }
```


## Return Value

The HTTP methods handling functions can return `dict`, `list`, `str`, `int`, **Pydantic Models**, etc.
They all will get converted to JSON by FastAPI.
