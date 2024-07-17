# 0x02-redis_basic|---------------|
| 0           | Writing strings to Redis                             | Create a `Cache` class with a `store` method to store data in Redis using a random key. Type-annotate `store` correctly.                                                                                                                                                                                                                                         | exercise.py   |
| 1           | Reading from Redis and recovering original type      | Update `Cache` with a `get` method to retrieve and convert data from Redis. Implement `get_str` and `get_int` methods.                                                                                                                                                                                                                                          | exercise.py   |
| 2           | Incrementing values                                  | Implement a `count_calls` decorator to count how many times `Cache` methods are called. Decorate `Cache.store` with `count_calls`.                                                                                                                                                                                                                               | exercise.py   |
| 3           | Storing lists                                        | Define a `call_history` decorator to store the history of inputs and outputs for a function. Decorate `Cache.store` with `call_history`.                                                                                                                                                                                                                        | exercise.py   |
| 4           | Retrieving lists                                     | Implement a `replay` function to display the history of calls of a particular function.                                                                                                                                                                                                                                                                         | exercise.py   |
| 5           | Implementing an expiring web cache and tracker       | Implement a `get_page` function to obtain HTML content from a URL, track access counts, and cache results with an expiration time of 10 seconds.                                                                                                                                                                                                                | web.py        |

## Detailed Task Table

| Task Number | Task Title                     | Subtasks/Details                                                                                                                                                                                                                                                                                                                                                                           |
|-------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | Writing strings to Redis       | - Create a `Cache` class<br>- Store a Redis client instance in `_redis`<br>- Flush the Redis instance using `flushdb`<br>- Implement `store` method to save data in Redis using a random key<br>- Type-annotate `store` method                                                                                                                                                           |
| 1           | Reading from Redis             | - Implement `get` method to retrieve data from Redis<br>- Use an optional `Callable` argument to convert data<br>- Implement `get_str` and `get_int` methods<br>- Conserve original `Redis.get` behavior if key does not exist                                                                                                                                                             |
| 2           | Incrementing values            | - Learn the `INCR` command<br>- Define `count_calls` decorator to count method calls<br>- Use method’s qualified name as key<br>- Increment count for key every time method is called<br>- Use `functools.wraps` to preserve original function properties<br>- Decorate `Cache.store` with `count_calls`                                                                                   |
| 3           | Storing lists                  | - Learn Redis commands `RPUSH`, `LPUSH`, `LRANGE`<br>- Define `call_history` decorator to store input/output history<br>- Use method’s qualified name with `":inputs"` and `":outputs"` for keys<br>- Use `rpush` to append input arguments as strings<br>- Execute wrapped function, store output with `rpush`<br>- Decorate `Cache.store` with `call_history`                       |
| 4           | Retrieving lists               | - Implement `replay` function to display function call history<br>- Display format: `Cache.store was called X times:`<br>- Example output: `Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f`                                                                                                                                                                                |
| 5           | Expiring web cache and tracker | - Implement `get_page` function to fetch HTML content from URL<br>- Use `requests` module<br>- Track URL access counts in key `"count:{url}"`<br>- Cache result with 10 seconds expiration<br>- Use [http://slowwly.robertomurray.co.uk](http://slowwly.robertomurray.co.uk) for testing<br>- Bonus: Implement with decorators                                                   |

## Usage

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tasks:
   ```bash
   python exercise.py
   python web.py
   ```
# Redis Basics Project Overview

This project is designed to help you learn to use the Redis NoSQL data storage application through Python3. The project is divided into several tasks, each focusing on different aspects and functionalities of Redis. Below is an overall summary of the project, including detailed descriptions of each task, their requirements, and the files involved.

## Project Structure

- **exercise.py**: Contains the main code for tasks related to basic Redis operations, such as storing and retrieving data, incrementing values, and managing call histories.
- **web.py**: Contains the code for implementing an expiring web cache and tracker.

## Tasks Overview

### Task 0: Writing Strings to Redis
- **Description**: Create a `Cache` class with methods to store data in Redis using random keys.
- **Requirements**:
  - Store a Redis client instance in `_redis`.
  - Flush the Redis instance using `flushdb`.
  - Implement a `store` method to save data in Redis using a random key.
  - Type-annotate the `store` method.
- **File**: `exercise.py`

### Task 1: Reading from Redis and Recovering Original Type
- **Description**: Implement methods to retrieve data from Redis and convert it back to its original type.
- **Requirements**:
  - Implement a `get` method with an optional `Callable` argument for data conversion.
  - Implement `get_str` and `get_int` methods.
  - Conserve original `Redis.get` behavior if the key does not exist.
- **File**: `exercise.py`

### Task 2: Incrementing Values
- **Description**: Implement a system to count how many times methods of the `Cache` class are called.
- **Requirements**:
  - Learn the `INCR` command.
  - Define a `count_calls` decorator to count method calls.
  - Use method’s qualified name as key.
  - Increment count for key every time the method is called.
  - Use `functools.wraps` to preserve original function properties.
  - Decorate `Cache.store` with `count_calls`.
- **File**: `exercise.py`

### Task 3: Storing Lists
- **Description**: Implement a decorator to store the history of inputs and outputs for a particular function.
- **Requirements**:
  - Learn Redis commands `RPUSH`, `LPUSH`, `LRANGE`.
  - Define a `call_history` decorator to store input/output history.
  - Use method’s qualified name with `":inputs"` and `":outputs"` for keys.
  - Use `rpush` to append input arguments as strings.
  - Execute wrapped function, store output with `rpush`.
  - Decorate `Cache.store` with `call_history`.
- **File**: `exercise.py`

### Task 4: Retrieving Lists
- **Description**: Implement a `replay` function to display the history of calls of a particular function.
- **Requirements**:
  - Implement `replay` function to display function call history.
  - Display format: `Cache.store was called X times:`.
  - Example output: `Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f`.
- **File**: `exercise.py`

### Task 5: Implementing an Expiring Web Cache and Tracker
- **Description**: Implement a web caching system with expiration and access tracking.
- **Requirements**:
  - Implement `get_page` function to fetch HTML content from URL.
  - Use `requests` module.
  - Track URL access counts in key `"count:{url}"`.
  - Cache result with 10 seconds expiration.
  - Bonus: Implement with decorators.
- **File**: `web.py`

## Usage Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tasks**:
   ```bash
   python exercise.py
   python web.py
   ```

## Conclusion

This project provides a comprehensive guide to understanding and using Redis with Python. By completing these tasks, you will gain practical experience in storing and retrieving data, managing call histories, implementing caching mechanisms, and more. Each task builds on the previous one, progressively enhancing your skills and knowledge in using Redis for various applications.
