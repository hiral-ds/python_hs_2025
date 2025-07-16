import functools

num = [12,56,74,98,52,102]
big = functools.reduce(lambda x,y: x if x>y else y,num)
small = functools.reduce(lambda x,y: x if x<y else y,num)
print("Maximum number is",big)
print("Minimum number is",small)

#sum list of numbers
number = [2,5,8,6,4]
sum = functools.reduce(lambda x,y :x+y,number)
print("Sum list of numbers",sum)

word = ["I","Love","You"]
add = functools.reduce(lambda x,y: x + ' ' + y , word)
print(add)

# find product of list
a = [10,20,30]
num = functools.reduce(lambda x,y: x*y , a)
print("Product of list",num)
  
a = pow(2,4)
print(a)