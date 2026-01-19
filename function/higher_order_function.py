# lambda or anonymous functions
def addition(x,y):
    return x + y

add =lambda a , b : a + b
print(add(3,4))


a = [(3,6), (1,4), (5,2)]
a.sort(key=lambda x: x[1])
print(a)