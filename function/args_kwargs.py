#Arbtrary Arguments (*args, **kwargs)

def addition(*args):
    print(args)
addition(1,2,"Nishan")

def keyword_arguments(**kwargs):
    print(kwargs)
keyword_arguments(name="Nishan", age=25, profession="Developer")

def total_sum(**kwargs):
    return sum(kwargs.values())

result = total_sum(a=10, b=20, c=30)
print("The total sum is:", result)
