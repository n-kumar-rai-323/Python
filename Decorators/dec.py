def decorator_me(func):
    def inner_fun():
        print("Before executing the function.")
        func()
    return inner_fun
@decorator_me
def message():
    print("This is the main function.")

# result = decorator_me(message)
# result()
message()