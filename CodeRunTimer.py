import time

def run_timer(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    duration = (end - start) * 1000  # ms
    print(f"Execution Time: {duration:.4f} ms")
    return result

# Sample function to test
def example_task():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Run timer on sample function
run_timer(example_task)
