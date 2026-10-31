import time
from functools import wraps
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        exec = end - start
        print(f"Функция '{func.__name__}' выполнилась за {exec:.6f} сек.")
        return result
    return wrapper

@time_it
def f(x):
    c = 0
    for i in range(x):
        c += i
    return c

result = f(10000000)