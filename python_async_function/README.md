# Holbertonschool Web back-end

## General 🧢
The `async` and `await` syntax in Python allows for asynchronous programming, enabling tasks to run concurrently without blocking the execution of other tasks. Asyncio, a built-in Python library, provides the framework for managing asynchronous operations. To execute an `async` program with asyncio, the asyncio.run() function is used to run the main entry point of the program. Concurrent coroutines, which are asynchronous functions, are executed using asyncio.create_task() or by gathering multiple coroutines with asyncio.gather(). This allows for parallel execution of tasks. Asyncio tasks represent individual units of work and can be created using asyncio.create_task(). Additionally, the random module in Python provides functions for generating random numbers and sequences, which can be useful for introducing randomness in asyncio applications, such as simulating user behavior in web applications or testing concurrent code with randomized inputs. Overall, `async` and `await` syntax, combined with asyncio, facilitate the creation of efficient and responsive asynchronous programs in Python, allowing for parallel execution of tasks and effective management of concurrent operations.

## Requirements 👮
- All files should start with `#!/usr/bin/env python3`
- All files should be executable
- Check pycodestyle
- Modules and classes should have documentations

## Tasks 🎱
0. The basics of async
    - Write an asynchronous coroutine that takes in an integer argument. Use `random`.
1. Let's execute multiple coroutines at the same time with async
    - Import `wait_random` from the previous python file. Write an async routine called `wait_n`that takes in 2 int arguments
2. Measure the runtime
    - From the previous file, import `wait_n`. Create a `measure_time` function with integers n and `max_delay` as arguments that measures the total execution time and returns total_time / n.
3. Tasks
    - Import `wait_random`. Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task.`
4. Tasks
    - Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

## Authors 🧞‍♀️
Sarah Boutier