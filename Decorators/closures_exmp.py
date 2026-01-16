def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

result = outer_func("Hello, World!")
result()

# Example 1: Simple message printer
def greet(name):
    def say_hello():
        print("Hello", name)
    return say_hello

call = greet("Nishan Kumar Rai")
call()

# Power Function 
def power(exponent):
    def raise_to(number):
        return number ** exponent
    return raise_to

square = power(2)
print(square(5))
 
# Counter
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
c = counter()
print(c())
print(c())
# Example 4: Function Logger (Decorator-style)
def logger(func_name):
    def log(message):
        print(f"{func_name}: {message}")
    return log
auth_log = logger("Authentication")
auth_log("User logged in successfully.")
# Example 5: Access Control (Advanced Closure)
def access_control(role):
    def check_access(user):
        if user==role:
            return "Access Granted"
        else:
            return "Access Denied"
    return check_access

admin = access_control("admin")
print(admin("customer"))

# Example 6: Closure with Mutable Data
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

result = outer_func("Hello, World!")
result()

# Example 1: Simple message printer
def greet(name):
    def say_hello():
        print("Hello", name)
    return say_hello

hello_nishan = greet("Nishan")
hello_nishan()

# Example 2: Power function
def power(exponent):
    def raise_to(number):
        return number ** exponent
    return raise_to

square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(5))    # 125


# Example 3: Counter
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

# Example 5: Access Control (Advanced Closure)
def access_control(role):
    def check_access(user_role):
        if user_role == role:
            return "Access granted"
        else:
            return "Access denied"
    return check_access

admin_access = access_control("admin")

print(admin_access("admin"))  # Access granted
print(admin_access("guest"))  # Access denied

# Example 6: Closure with Mutable Data
def shopping_cart():
    items = []
    def add_item(item):
        items.append(item)
        return items
    return add_item
cart = shopping_cart()
print(cart("apple"))  # ['apple']
print(cart("banana")) # ['apple', 'banana']