def decorator_me(func):
    def inner_fun():
        func()
    return inner_fun

def message():
    print("This is the main function.")

result = decorator_me(message)
result()

# Example: Admin access check using decorator
def admin_required(func):
    def wrapper():
        role =input("Enter your role: ")
        if role.lower() == "admin":
            print("Access granted to admin panel.")
            return func()
        else:
            return print("Access denied. Admins only.")
    return wrapper

# @admin_required
def delete_user():
    print("User deleted successfully.")
# print(delete_user())
admin_access = admin_required(delete_user)
print(admin_access())




# Another example (bonus): Login attempts limit 🔒

def limit_attempts(func):
    attempts =0

    def wrapper():
        nonlocal attempts
        if attempts <3:
            attempts +=1
            return func()
        else:
            return print("Maximum login attempts exceeded.")
    return wrapper

def access_system():
    print("system accessed successfully.")

limited_access = limit_attempts(access_system)
print(limited_access())  # 1st attempt
print(limited_access())  # 2nd attempt
print(limited_access())  # 3rd attempt
print(limited_access())  # 4th attempt - should be denied



# 1️⃣ Decorator using *args and **kwargs
def login_required(func):
    def wrapper(*args, **kwargs):
        password = input("Enter password to access: ")
        if password =="admin123":
            print("Login successful.")
            return func(*args, **kwargs)
        else:
            print("Login failed. Incorrect password.")
            return None
    return wrapper

@login_required
def view_profile(username):
    print(f"Viewing profile of {username}.")

print(view_profile("Nishan Kumar Rai"))  # Without decoratorator
# secured_view = login_required(view_profile)
# print(secured_view("Nishan Kumar Rai"))  # Try with correct and incorrect password

# 2️⃣ Decorator with arguments (custom message)

def permission_required(role):
    def decorator(func):
        def wrapper():
            user_role =input("Enter your role:")
            if user_role.lower() == role.lower():
               return func()
            else:
                print(f"Permission denied. {role} role required.")
        
        return wrapper
    return decorator
@permission_required("admin")
def shutdown_system():
    return print("System is shutting down...")
# secured_shutdown = permission_required("admin")(shutdown_system)
# print(secured_shutdown())  # Try with different roles
print(shutdown_system())  # Try with different roles