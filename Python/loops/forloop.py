# For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is "for in" loop which is similar to foreach loop in other languages.

n = 4
for i in range(0, n):
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break
  
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
print(x)

# remove vowel form string
# word = input("Enter word : ")
# vowel = "aeiou"
# for i in word:
#     if i in vowel:
#         word = word.replace(i,'')
# print(word)


# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# for x in range(6):
#   print(x)

