import os
clear = lambda: os.system("clear")
clear()


def remainder(num): 
    return lambda num: num % 2
remainder5 = remainder(5)
remainder4 = remainder(4)

print(remainder5(5))
print(remainder4(4))


def product(x, y): 
    return lambda x,y: x*y
product = product(2,3)
print(product(2, 3))

def testfunc(num):
    return lambda x: x* num
result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

result10 = lambda x: x * 10
result100 = lambda x: x * 100 

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

def myfunc(x):
    if x > 7:
        return x
    
result = list(filter(myfunc, numbers_list))
print(result)
result = list(filter(lambda num:num>7,numbers_list))
print(result)


def addition(n):
    return n + n
numbers = [1,2,3,4]
result = list(map(addition,numbers))
print(result)

result = list(map(lambda x: x +x,numbers))
print(result)

numbers = [1,2,3,4]
numbers2 = [4,5,6,7]
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)