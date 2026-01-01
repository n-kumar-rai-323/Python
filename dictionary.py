phoneBook = {
    'name': 'Nishan Rai',
    'age': 25,
    'is_student': True,
    'courses': ['Math', 'Science', 'Art'],
    'address': {
        'street': '123 Main St',
        'city': 'Kathmandu',
        'zip': '44600'
    }
}
print(phoneBook)
phoneBook.get('name')  # 'Nishan Rai'
print(phoneBook['age'])  # 25
print(phoneBook['courses'][1])  # 'Science'
print(phoneBook.get('phone', 'Not Found'))  # 'Not Found'
phoneBook.pop('is_student')  # removes the key 'is_student'
print(phoneBook)
phoneBook['age'] = 26  # updates the age to 26
print(phoneBook)