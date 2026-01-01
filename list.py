nums = 45, 23, 67, 89, 12
print(nums)
# what is list ?
# list is a collection of items in a particular order
# Python lists are mutable.
#This means that after a list is created, its contents can be modified without creating a new list object. You can add, remove, or change elements within the existing list.

numbers = [45, 23, 67, 89, 12]
print(numbers)
print(numbers[0])  # 45
print(numbers[2:4])  # [67, 89] 

data = ["Nishan", 25, True, 4.99, "Rai", [1, 2, 3]]
mix =[nums,numbers,data]
print(mix)
print(len(mix))
print(mix[0][0])
print(mix[2][5][0])



numbers.append(100) # adds 100 at the end of the list
print(numbers)
numbers.count(23) # counts how many times 23 appears in the list
print(numbers)
numbers.insert(1, 200) # inserts 200 at index 1
print(numbers)
numbers.remove(67) # removes 67 from the list
print(numbers)
numbers.pop() # removes the last item from the list
print(numbers)
numbers.pop(1) # removes item at index 1
print(numbers)
del numbers[0] # deletes item at index 0
print(numbers)
numbers.extend([300, 400, 500]) # extends the list by adding multiple items
print(numbers)
numbers.reverse() # reverses the list
print(numbers)
numbers.sort() # sorts the list in ascending order
print(numbers)
numbers.sort(reverse=True) # sorts the list in descending order
print(numbers)
