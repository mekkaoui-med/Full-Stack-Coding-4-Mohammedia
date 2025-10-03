def calculation(a,b):
    add = f'the addition of {a} and {b} is : a + b =  {a+b} '
    subt = f'the subtraction of {a} and {b} is :a - b = {a - b}'
    return add,subt
add, subt= calculation(40, 10)

print(add)
print(subt)