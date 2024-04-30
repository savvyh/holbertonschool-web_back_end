# Web Back-End - Pagination

## General 📃
To paginate with simple parameters, like page and page_size, servers fetch specific dataset subsets based on client requests. Hypermedia metadata pagination adds navigation links to responses, enhancing user interaction. Deletion-resilient pagination employs cursor-based methods, ensuring consistency despite dataset changes.

## Requirements :anchor:
* All files should start with #!/usr/bin/env python3
* All files should be executable
* Check pycodestyle
* Modules and classes should have documentations
* Setup: `Popular_Baby_Names.csv`

## Tasks ⚫
0. Simple helper function:
    - Write a function named `index_range` that takes two integer arguments `page` and `page_size`.
    - The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
1. Simple pagination:
    - Copy `index_range` from the previous task and the following class into the code.
    - Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.
2. Hypermedia pagination:
    - Replicate code from the previous task.
    - Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing specific key-value pairs.
3. Deletion-resilient hypermedia pagination:
    - The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
    - Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10.

## Authors 🧞‍♀️
Sarah Boutier