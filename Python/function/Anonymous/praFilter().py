l1 = [1,2,3,4,5,6,7,8,9]
odd = lambda x: x %2 != 0
odd_list = list(filter(odd,l1))
print("Odd numbers list",odd_list)

l2 = [1,2,-5,6,-8,9,-4,5,3,-7]
positive = lambda x: x > 0
posi_li = list(filter(positive,l2))
print("Positive number list",posi_li)

negative = lambda y: y < 0
nega_li = list(filter(negative,l2))
print("Negative number list",nega_li)