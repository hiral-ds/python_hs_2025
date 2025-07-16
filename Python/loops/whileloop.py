# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# With the break statement we can stop the loop even if the while condition is true:
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    pass
  print(i)



