def login_required(func):
    def inner_function():
        pw = input("Enter your password:")
        if pw == "admin123":
            print("Login successful!")
            return func()
        else:
            print("Login failed.")
            return None
    return inner_function


@login_required
def get_data():
    return "Sensitive Data: [User Information]"
print(get_data())