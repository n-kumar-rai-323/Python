# def message():
#     print("This is a message from the exception handling recursion module.")
#     message()  # Recursive call without a base case
# # message()


value = 0

def recursive_function():
    global value
    try:
        value += 1
        if value > 10:
            return
        print("Recursion depth:", value)
        recursive_function()   # recursive call
    except RecursionError:
        print("Recursion limit reached at value:", value)

recursive_function()
