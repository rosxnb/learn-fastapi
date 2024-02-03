Python Decorators is a design pattern where the decorator function takes another function as argument
and executes the passed function in an environment defined by the decorator.


## Function Definitions

```python
def my_decorator(foo):
    def my_wrapper(*args, **kwargs):
        print(f"my_wrapper executed before {foo.__name__}")
        return foo(*args, **kwargs)
    return my_wrapper

def func():
    print("func() is executed")
```


## No Decorator
```python
decorated_func = my_decorator(func)
decorated_func()
```


## With Decorator
```python
@my_decorator
def func():
    print("func() is executed")

func()
```


## Preserve Name

With function decorators, the function passed as argument doesn't retain its original name.
```python
>>> func.__name__
# my_wrapper
```

To preserve the name of passed function, we can do following
```python
from functools import wraps

def my_decorator(foo):

    @wraps(foo)
    def my_wrapper(*args, **kwargs):
        print(f"my_wrapper executed before {foo.__name__}")
        return foo(*args, **kwargs)

    return my_wrapper
```


## Pass Decorator Argument
```python
def prefix_decorator(arg):

    def my_decorator(foo):
        def my_wrapper(*args, **kwargs):
            print(arg, f"my_wrapper executed before {foo.__name__}")
            return foo(*args, **kwargs)
        return my_wrapper

    return my_decorator

@prefix_decorator("Welcome: ")
def func():
    print("func() is executed")


# Vanilla way
f = prefix_decorator("Okay: ")(func)
f()
```


## Class Decorator
```Python
class CustomDecorator:
    def __init__(self, foo):
        self.func = foo

    def __call__(self, *args, **kwargs):
        print(f"my_wrapper executed before {foo.__name__}")
        return self.func(*args, **kwargs)

```
