import time
def exe_time(func):
    def inner_func():
        start = time.time()
        a = func()
        end = time.time()
        print(f"Execution time: {end - start}")
        return a
    return inner_func

@exe_time
def test_func():
    for i in range(100000000):
        pass
    return "Function execution completed."
print(test_func())


