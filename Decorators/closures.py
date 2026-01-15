# ---------- Decorator definition ----------
def to_upper(func):
    def inner_func():
        value = func()
        return value.upper()
    return inner_func


# ---------- Closure example ----------
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

hi_func = outer_func("Hello, World!")
hi_func()   # Output: Hello, World!


# ---------- Decorator usage ----------
@to_upper
def decorator_upper():
    return "Nishan Kumar Rai"

print(decorator_upper())


# ---------- Another decorator ----------
def decorator_me(func):
    def inner_fun():
        print("Before executing the function.")
        func()
    return inner_fun

@decorator_me
def message():
    print("This is the main function.")

message()
