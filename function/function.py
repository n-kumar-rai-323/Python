#what is function in python
# A function in Python is a reusable block of code that performs a specific task.
#  It is defined using the 'def' keyword, followed by the function name and parentheses. 
# Functions can take input parameters, execute a series of statements, and return a value.




def add (a,b):
    sum = a + b
    return sum
result = add(5,6)
print("The sum is:", result)


def greet(num1, num2):
    return num1 + num2

print(greet("Hello, ", "World!"))



def argment_example(arg1, ):
    print("First argument:", arg1)
    print("Other arguments:", args2)
    return arg1, args2

print(argment_example("Nishan", "Rai", "is", "a", "developer."))



    