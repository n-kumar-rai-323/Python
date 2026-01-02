from Decorators import to_upper

def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func
hi_func = outer_func("Hello, World!")
hi_func()  # Output: Hello, World!

@to_upper
def decorator_upper():
    return ("Nishan Kumar Rai")


print(decorator_upper())