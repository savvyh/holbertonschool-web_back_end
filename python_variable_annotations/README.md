# Holbertonschool Web back-end

## General 🧢
In Python 3, type annotations provide a way to specify the types of variables and function parameters, aiding in code readability and maintenance. By adding annotations to function signatures and variables, developers can explicitly declare the expected types, enhancing code documentation and enabling static analysis tools like Mypy to catch type-related errors early in the development process. Python's dynamic typing system still allows for flexibility, but type annotations offer additional clarity, especially in larger codebases. Duck typing, a fundamental concept in Python, focuses on an object's behavior rather than its type. This allows objects of different types to be used interchangeably if they support the required methods or attributes. Mypy is a static type checker for Python that can analyze code with type annotations and detect type-related issues such as type mismatch errors or missing type annotations. Integrating Mypy into the development workflow can help ensure code correctness and reliability, particularly in projects where type safety is crucial.

## Requirements 👮
- All files should start with `#!/usr/bin/env python3`
- All files should be executable
- Check pycodestyle
- Modules and classes should have documentations

## Tasks 🎱
0. Basic annotations - add
    - Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
1. Basic annotations - concat
    - Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.
2. Basic annotations - floor
    - Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
3. Basic annotations - to string
    - Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
4. Define variables
    - Define and annotate the following variables with the specified values.
5. Complex types - list of floats
    - Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
6. Complex types - mixed list
    - Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
7. Complex types - string and int/float to tuple
    - Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
8. Complex types - functions
    - Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
9. Let's duck type an iterable object
    - Annotate the below function’s parameters and return values with the appropriate types
  
## Authors 🧞‍♀️
Sarah Boutier
