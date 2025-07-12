li = [2,3,4,5,6]
square = lambda x: x*x
squ_li = list(map(square,li))
print("Square of number in list",squ_li)

#Add two list
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,5]
add = lambda x,y: x+y
add_l = list(map(add,l1,l2))
print("Addition of two list",add_l)

# String to list
a = "Python"
word = lambda x:x
word1 = list(map(word,a))
print(word1)