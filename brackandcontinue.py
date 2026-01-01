data = [2, "Nishan", 4.5, "Python", 10, "Code", 3.14, "AI"]

for value in range(10):
    if value % 2 == 0:
        continue
    print(f"{value} is an odd number.")

for item in range(10):
    if item > 5:
        break
    print(item)
print("Loop ended.")