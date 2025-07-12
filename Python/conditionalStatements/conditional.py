# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#take 3 num from user and check which is smallest and print.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c:
    print("'if block was executed' largest number is : ",a)
elif b > a and b > c:
    print("'elif block was executed' largest number is :",b)
else:
    print("'else block was executed' largest number is : ",c)

print("-"*50)

#Take a palindrome word and print same word after reversing
word = input("Enter string : ")
a = word[::-1]
if word == a:
    print("String is palindrome : ",word)
else:
    print("String is not palindrome : ",word)