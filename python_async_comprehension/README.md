# Python Async Comprehension

## General 🧢
Writing an asynchronous generator in Python involves defining a coroutine function using the `async def` syntax and yielding values using the yield statement within an async for loop. This allows for asynchronous iteration over a potentially infinite sequence of values, with each value being generated asynchronously. Async comprehensions provide a concise way to construct asynchronous generators by combining the async for loop syntax with a comprehension expression, allowing for the creation of asynchronous sequences based on iterables, with each element being processed asynchronously. Type-annotating generators involves specifying the types of values yielded by the generator function using type hints, including the return type annotation for the generator function itself. This ensures clarity and helps in understanding the structure and behavior of asynchronous generators, aiding in the development of robust and maintainable asynchronous codebases.

## Requirements 👮
- All files should start with `#!/usr/bin/env python3`
- All files should be executable
- Check pycodestyle
- Modules and classes should have documentations

## Tasks 🎱
0. Async Generator
    - Write a coroutine called `async_generator` that takes no arguments.
1. Async Comprehensions
    - Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.
    - The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.
2. Run time for four parallel comprehensions
    - Import `async_comprehension` from the previous file and write a measure_runtime coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather.
    - `measure_runtime` should measure the total runtime and return it.

## Authors 🧞‍♀️
Sarah Boutier