FastAPI heavily uses data annotations to have better editor support and type error detection during development.
Apart from that, it also uses data annotations to:

- **Define requirements** from request path parameters, query parameters, headers, bodies, dependencies, etc
- **Convert data** from the request to the required type
- **Validate data** coming from each request. This is done by [Pydantic](https://docs.pydantic.dev/latest/)
- **Generating** automatic errors returned to the client when the data is invalid
- **Document** the API using OpenAPI


### Basic Types

- `int`
- `float`
- `bool`
- `bytes`


### Derived Types

- `list[str]`
- `dict[str, int]`
- `tuple[float]`


### Alternative Types

- `int | None` or `Union[int, None]` or `Optional[int]`
- `str | float` or `Union[str, float]`

> Note: `Union` and `Optional` are defined in `typing` package


### User Defined Types

We can also annotate a variable to be a data type of user define class.


### Pydantic Models

[Pydantic](https://docs.pydantic.dev/latest/) is used to declare the shape of data.
The shape is specified as class with attributes with each attributes having a type.

```python
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)

print(user)
# User(id=123, name='John Doe', signup_ts=datetime.datetime(2017, 6, 1, 12, 22), friends=[1, 2, 3])
```


### Metadata Annotations

```python
from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```

The first type parameter is the actual data type annotation then rest is metadata 
which is used to tell FastAPI how we want our application to behave.
