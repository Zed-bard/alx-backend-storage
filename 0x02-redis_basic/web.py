import requests
import redis
import time
from functools import wraps

# Connect to the local Redis server
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(expire_time=10):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Track the number of times a URL is accessed
            count_key = f"count:{url}"
            cache.incr(count_key)

            # Check if the page is already cached
            cached_page = cache.get(url)
            if cached_page:
                print("Cache hit")
                return cached_page.decode('utf-8')

            # If not cached, fetch the page
            print("Cache miss")
            page_content = func(url)
            cache.setex(url, expire_time, page_content)
            return page_content
        return wrapper
    return decorator

@cache_page(expire_time=10)
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"

    # First access, should be a cache miss
    print(get_page(url))

    # Wait for 5 seconds and access again, should be a cache hit
    time.sleep(5)
    print(get_page(url))

    # Wait for 10 seconds and access again, should be a cache miss (cache expired)
    time.sleep(10)
    print(get_page(url))

    # Print the number of times the URL was accessed
    print(f"URL accessed {cache.get(f'count:{url}').decode('utf-8')} times")

