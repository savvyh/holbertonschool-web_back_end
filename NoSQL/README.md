# Back End - NoSQL 

## General ♟️
NoSQL, or Not Only SQL, refers to a class of database management systems that offer a flexible approach to data storage and retrieval compared to traditional SQL databases. Unlike SQL databases, which rely on a fixed schema and tables to organize data, NoSQL databases can handle various types of data structures, including semi-structured and unstructured data. ACID, or Atomicity, Consistency, Isolation, and Durability, is a set of properties that ensure the reliability of database transactions. Document storage is a type of NoSQL database model that stores data in flexible, self-describing document formats such as JSON or XML. There are several types of NoSQL databases, including document-oriented, key-value, column-oriented, and graph databases, each tailored to different data types and use cases. NoSQL databases offer benefits such as scalability, flexibility, and high performance, making them suitable for applications with large volumes of rapidly changing data. Querying information from a NoSQL database typically involves using specialized query languages or APIs provided by the database system to retrieve data based on specific criteria. Inserting, updating, and deleting information from a NoSQL database can be achieved using the appropriate commands or methods provided by the database system, often through APIs or programming interfaces. MongoDB, a popular NoSQL database, can be used by installing and configuring the MongoDB server, then interacting with the database using its native query language or through various programming languages using the MongoDB drivers and APIs.

## Requirements 🚓
- MongoDB Command File : 
    - The first line of all files should be a comment: `// my comment`
    - Install `MongoDB` 4.2 in Ubuntu 18.04 : 
        * import public key : `sudo apt-get install gnupg curl`
        * install mongoDB package : `sudo apt-get install -y mongodb-org`
        * Use `container-on-demand` to run MongoDB

- Python Scripts :
    - All files should start with `#!/usr/bin/env python3`
    - All files should be executable
    - Check pycodestyle
    - Modules and classes should have documentations

## Tasks ⚫
0. List all databases
    - Write a script that lists all databases in MongoDB.
1. Create a database
    - Write a script that creates or uses the database `my_db`
2. Insert document
    - Write a script that inserts a document in the collection `school`:
        * The document must have one attribute name with value `Holberton school`
        * The database name will be passed as option of `mongo` command.
3. All documents
    - Write a script that lists all documents in the collection `school`:
        * The database name will be passed as option of `mongo` command
4. All matches
    - Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
        * The database name will be passed as option of `mongo` command
5. Count
    - Write a script that displays the number of documents in the collection `school`:
        * The database name will be passed as option of `mongo` command
6. Update
    - Write a script that adds a new attribute to a document in the collection `school`:
        * The script should update only document with `name="Holberton school"` (all of them)
        * The update should add the attribute address with the value `972 Mission street`
        * The database name will be passed as option of `mongo` command.
7. Delete by match
    - Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
        * The database name will be passed as option of `mongo` command
8. List all documents in Python
    - Write a Python function that lists all documents in a collection:
        * Prototype: `def list_all(mongo_collection):`
        * Return an empty list if no document in the collection
        * `mongo_collection` will be the pymongo collection object
9. Insert a document in Python
    - Write a Python function that inserts a new document in a collection based on kwargs:
        * Prototype: `def insert_school(mongo_collection, **kwargs):`
        * `mongo_collection` will be the pymongo collection object
        * Returns the `new _id`
10. Change school topics 
    - Write a Python function that changes all topics of a school document based on the name:
        * Prototype: `def update_topics(mongo_collection, name, topics):`
        * `mongo_collection` will be the pymongo collection object
        * `name` (string) will be the school name to update
        * `topics` (list of strings) will be the list of topics approached in the school
11. Where can I learn Python?
    - Write a Python function that returns the list of school having a specific topic:
        * Prototype: `def schools_by_topic(mongo_collection, topic):`
        * `mongo_collection` will be the pymongo collection object
        * `topic`(string) will be topic searched
12. Log stats
    - Write a Python script that provides some stats about Nginx logs stored in MongoDB.
        * Use this dump as data sample : `dump.zip`
        * Database: `logs`
        * Collection: `nginx`
        * The output of your script must be exactly the same as the example : 

## Authors 🧞‍♀️
Sarah Boutier