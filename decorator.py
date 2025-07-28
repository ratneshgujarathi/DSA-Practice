from functools import wraps
import time

def time_counter(func):  
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time = end_time - start_time
        print(f"Execution time: '{func.__name__}': {total_time:.5f} seconds")
        return result
    
    return wrapper

@time_counter
def slow_function():
    time.sleep(2)

slow_function()