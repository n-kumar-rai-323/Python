a = [1,2,3,4,5,6,7,8,9,10]
iter_a =iter(a)
while True:
    try:
        element = next(iter_a)
        print(element)
    except StopIteration:
        break

s = "Nishan Rai"
new_s = ""
char = input("Enter a character to search: ")
for i in s:
    if i.lower() == char.lower():
        continue
    new_s=new_s + i
print(new_s)


a = [1,2,3,4,5]
s = ''
for i in a:
    s += f"{i}"
print(s)