try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input. Please enter a valid integer.")

# Take two numbers an input and add those numbers. handle the possible exceptions.
try:
    numOne = int(input("Enter first number: "))
    numTwo = int(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
else:
    sum = numOne + numTwo
    print(f"The sum of {numOne} and {numTwo} is {sum}.")    

# Create a function to divide a number by another number. Handle the possible exceptions.
def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {numerator} divided by {denominator} is {result}.")

divide_numbers()

# create a dictionary student with keys id,name,age,department. Take a input from the user, which info (id, name, age or department) he wants to access and print the result. Handle the possible exception 
student = {
    "id": 1,
    "name": "Alice",
    "age": 20,
    "department": "Computer Science"
}
try:
    key = input("Enter the information you want to access (id, name, age, department): ")
    print(student[key])
except KeyError:
    print("Invalid key. Please enter a valid key (id, name, age, department).")