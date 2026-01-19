a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_even_numbers(num):
#     return num % 2 == 0

# result = filter(get_even_numbers, a)
result2 = filter(lambda x:x%2==0,a)
print(list(result2))

students=[
    {'name':'Nishan', 'age':24},
    {'name':'Ravi', 'age':19},
    {'name':'Sita', 'age':22},
    {'name':'Gita', 'age':17}]

result3 = filter(lambda student: student['age']>=20, students)
print(list(result3))

result4=filter(lambda x: x['age'] >=20 and x['name'].startswith('N'), students)
print(list(result4))

result5=map(lambda s: s['name'],
            filter(lambda x: x['age']>=20, students))
print(list(result5))

result = list(filter(
    lambda s: s.get('age', 0) >= 20,
    students
))

print(result)