class A:
    a = 1

    def __init__(self, b):
        self.b = b

obj1 = A(2)
print(obj1.a)  # Output: 1


class Student:
    name = "Nishan Rai"

student1 =Student()
print(student1.name)

class Car:
    color = "Red"
    brand = "Toyota"
car1 = Car()
print(car1.color)
print(car1.brand)


class Person:
   
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Person Created")

person1 = Person("Nishan Rai", 85)
print(person1.name)
print(person1.marks)



class Details:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name:{self.name}, Age:{self.age}")

details = Details("Nishan Rai", 20)
details.info()

class Employee:
    company = "Google"
    count = 0

    def __init__(self,name):
        self.name = name
        Employee.count +=1
e1 = Employee("Nishan Rai")
el2 = Employee("John Doe")
print(Employee.count)

# Exercise 6: Private Attribute
class Bank:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    def show_balance(self):
        print("Balance:", self.__balance)

# Exercise 11: Mini Project – Bank Account
class Account:
    def __init__(self, name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance=self.balance + amount
        print(f"Deposited {amount}. New balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(f"withdrow {amount}. New balance is {self.balance}")
    def show(self):
        print(f"Account holder: {self.name}, Balance:{self.balance}")

# user1 = Account("Nishan Kumar Rai", 1000)
# user1.deposit(500)
# user1.withdraw(1500)
# print(user1.show())

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def show(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")


# ---- USER INPUT ----
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

user1 = Account(name, balance)

# ---- OPTIONAL DEPOSIT ----
choice = input("Do you want to deposit? (yes/no): ").strip().lower()
if choice == "yes":
    deposit_amount = int(input("Enter deposit amount: "))
    user1.deposit(deposit_amount)

# ---- OPTIONAL WITHDRAW ----
choice = input("Do you want to withdraw? (yes/no): ").strip().lower()
if choice == "yes":
    withdraw_amount = int(input("Enter withdraw amount: "))
    user1.withdraw(withdraw_amount)

user1.show()
