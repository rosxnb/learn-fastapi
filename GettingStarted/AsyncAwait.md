`async` and `await` keywords are used to do **concurrent** programming in python.
> Note: concurrent and parallel programming are two different concepts.

In FastAPI,

- The normal `def` defined function gets added to **external threadpool** that is then awaited.
- The `async def` defined function should be `await`ed when calling it in code.
- For lightweight functions, not handling IO or computation heavy task, use `async def`.
- If not sure, use normal `def`.


### async and await
More in-depth explanation on the subject can be found [here](https://github.com/AndreLouisCaron/a-tale-of-event-loops?tab=readme-ov-file).

- To create a coroutine object, use `async` keyword
```python
async def foo():
    pass

>>> print(foo())
# <coroutine object foo at 0x10d2b3060>
```


- To execute a coroutine object, use `await` keyword. This creates **event-loop** to execute the coroutine
```python
async def main():
    await foo()

# import asyncio
# asyncio.run(foo())
```


- To not block following lines with `await` keyword, use `asyncio.create_task`
```python
import asyncio

async def foo(text):
    print("foo() starts")
    print("before sleep in foo:", text)
    await asyncio.sleep(5)
    print("after sleep in foo:", text)
    print("foo() finished")

async def main():
    print("main() starts")
    task = asyncio.create_task(foo('greetings'))
    print("main() finished")
    await task

asyncio.run(main())
```

