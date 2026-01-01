a = 5
print(id(a))  # prints the memory address of variable 'a'
a = 10
print(id(a))  # prints the new memory address of variable 'a' after reassignment

name = "Nishan"
print(id(name))  # prints the memory address of variable 'name'
name1 = "Nishan Rai"
print(id(name1))  # prints the memory address of variable 'name1'

print(name == name1)  # compares the values of 'name' and 'name1'