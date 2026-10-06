#Question 2
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def slow_add(a,  b):
    import time
    time.sleep(1)
    return a + b

print(slow_add(5,6))

#Question 3

def timer(precision=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed = round(end_time - start_time, precision)
            print(f"Execution time for {func.__name__}: {elapsed} seconds")
            return result
        return wrapper
    return decorator

@timer(precision=3)
def slow_add(a, b):
    time.sleep(1)
    return a + b

print(slow_add(5, 6))

#Question6
class FileLogger():
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "a")
        print(f"Opening {self.filename}")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(f"Closing {self.filename}")
    def write(self, msg):
        self.file.write(msg + "\n")

with FileLogger("log.txt") as logger:
    logger.write("first line")
    logger.write("second line")
    raise ValueError("test")