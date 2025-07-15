import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[START] Function '{func.__name__}' started at {time.ctime(start_time)}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[END] Function '{func.__name__}' ended at {time.ctime(end_time)}")
        print(f"[INFO] Execution time: {end_time - start_time:.4f}s")
        print(f"[INFO] Arguments: args={args}, kwargs={kwargs}")
        print("-" * 40)
        return result
    return wrapper

# Example function 1
@log_execution
def add(a, b):
    time.sleep(1)
    return a + b

# Example function 2
@log_execution
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"

# Demonstration
print(add(10, 20))
print(greet("Hiral"))