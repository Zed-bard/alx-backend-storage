
# 0x01-NoSQL

This project contains tasks for learning to use the MongoDB NoSQL database application.

## General Summary

This project involves learning to use the MongoDB NoSQL database application through a series of tasks. Each task focuses on a specific aspect of MongoDB, ranging from basic operations like listing databases and inserting documents to more complex functions such as updating documents, counting records, and filtering data using regex. Additionally, Python scripts are used to interact with MongoDB, providing functionalities like listing documents, inserting records, updating topics, and aggregating data for log statistics. The tasks are designed to build a comprehensive understanding of MongoDB's capabilities and how to utilize them effectively within Python programs.

## Requirements

### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- All your files should end with a new line.
- The first line of all your files should be a comment: `// my comment`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of your files will be tested using `wc`.

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
- All your functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)').
- Your code should not be executed when imported (by using `if __name__ == "__main__":`).

## Tasks To Complete

| Task Number | Task Description |
|-------------|------------------|
| 0 | **List all databases**<br/>[0-list_databases](0-list_databases) contains a MongoDB script that lists all databases in MongoDB. |
| 1 | **Create a database**<br/>[1-use_or_create_database](1-use_or_create_database) contains a MongoDB script that creates or uses the database `my_db`. |
| 2 | **Insert document**<br/>[2-insert](2-insert) contains a MongoDB script that inserts a document in the collection `school`:<br/>- The document must have one attribute `name` with value “Holberton school”.<br/>- The database name will be passed as an option of `mongo` command. |
| 3 | **All documents**<br/>[3-all](3-all) contains a MongoDB script that lists all documents in the collection `school`:<br/>- The database name will be passed as an option of `mongo` command. |
| 4 | **All matches**<br/>[4-match](4-match) contains a MongoDB script that lists all documents with `name="Holberton school"` in the collection `school`:<br/>- The database name will be passed as an option of `mongo` command. |
| 5 | **Count**<br/>[5-count](5-count) contains a MongoDB script that displays the number of documents in the collection `school`:<br/>- The database name will be passed as an option of `mongo` command. |
| 6 | **Update**<br/>[6-update](6-update) contains a MongoDB script that adds a new attribute to a document in the collection `school`:<br/>- The script should update only document with `name="Holberton school"` (all of them).<br/>- The update should add the attribute `address` with the value “972 Mission street”.<br/>- The database name will be passed as an option of `mongo` command. |
| 7 | **Delete by match**<br/>[7-delete](7-delete) contains a MongoDB script that deletes all documents with `name="Holberton school"` in the collection `school`:<br/>- The database name will be passed as an option of `mongo` command. |
| 8 | **List all documents in Python**<br/>[8-all.py](8-all.py) contains a Python function that lists all documents in a collection:<br/>- Prototype: `def list_all(mongo_collection):`.<br/>- Return an empty list if no document in the collection.<br/>- `mongo_collection` will be the `pymongo` collection object. |
| 9 | **Insert a document in Python**<br/>[9-insert_school.py](9-insert_school.py) contains a Python function that inserts a new document in a collection based on `kwargs`:<br/>- Prototype: `def insert_school(mongo_collection, **kwargs):`.<br/>- `mongo_collection` will be the `pymongo` collection object.<br/>- Returns the new `_id`. |
| 10 | **Change school topics**<br/>[10-update_topics.py](10-update_topics.py) contains a Python function that changes all topics of a school document based on the name:<br/>- Prototype: `def update_topics(mongo_collection, name, topics):`.<br/>- `mongo_collection` will be the `pymongo` collection object.<br/>- `name` (string) will be the school name to update.<br/>- `topics` (list of strings) will be the list of topics approached in the school. |
| 11 | **Where can I learn Python?**<br/>[11-schools_by_topic.py](11-schools_by_topic.py) contains a Python function that returns the list of school having a specific topic:<br/>- Prototype: `def schools_by_topic(mongo_collection, topic):`.<br/>- `mongo_collection` will be the `pymongo` collection object.<br/>- `topic` (string) will be topic searched. |
| 12 | **Log stats**<br/>[12-log_stats.py](12-log_stats.py) contains a Python script that provides some stats about Nginx logs stored in MongoDB:<br/>- Database: `logs`.<br/>- Collection: `nginx`.<br/>- Display:<br/>  - First line: `x logs` where `x` is the number of documents in this collection.<br/>  - Second line: `Methods:`.<br/>  - 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order.<br/>  - One line with the number of documents with:<br/>    - `method=GET`.<br/>    - `path=/status`.<br/>  - Example:<br/>    ```log<br/>    94778 logs<br/>    Methods:<br/>        method GET: 93842<br/>        method POST: 229<br/>        method PUT: 0<br/>        method PATCH: 0<br/>        method DELETE: 0<br/>    47415 status check<br/>    ```<br/>- You can use this dump as data sample: [dump.zip](dump.zip). |
| 13 | **Regex filter**<br/>[100-find](100-find) contains a MongoDB script that lists all documents with `name` starting by `Holberton` in the collection `school`:<br/>- The database name will be passed as an option of the `mongo` command. |
| 14 | **Top students**<br/>[101-students.py](101-students.py) contains a Python function that returns all students sorted by average score:<br/>- Prototype: `def top_students(mongo_collection):`.<br/>  - `mongo_collection` will be the `pymongo` collection object.<br/>- The top must be in descending order of average score.<br/>- The average score must be part of each item returned with key = `averageScore`.<br/>- A sample document in the collection is shown below:<br/>  ```json<br/>  {<br/>    "name": "Julia",<br/>    "topics": [<br/>      { "title": "Algo", "score": 10.5 },<br/>      { "title": "C", "score": 10.2 },<br/>      { "title": "Python", "score": 10.1 }<br/>    ]<br/>  }<br/>  ``` |
| 15 | **Log stats - new version**<br/>[102-log_stats.py](102-log_stats.py) improves [12-log_stats.py](12-log_stats.py) by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:<br/>- The top 10 IPs must be sorted. |
