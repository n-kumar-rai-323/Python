# map function 
# def map_function(func, iterable):
a = [1, 2, 3, 4, 5]
def multiple_by_two(x):
    return x * 2
result=map(multiple_by_two,a )
print(list(result))
