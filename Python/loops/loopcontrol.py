# Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. 


# The continue statement in Python returns the control to the beginning of the loop.
# The continue statement is used to skip the current iteration of a loop and move to the next iteration. It is useful when we want to bypass certain conditions without terminating the loop.

# for letter in 'lernpython':
#     if letter == 'e' or letter == 't':
#         continue
#     print('Current Letter :', letter)



# The break statement in Python brings control out of the loop.

# break statement is used to exit the loop prematurely when a specified condition is met. In this example, the loop breaks when the letter is either 'e' or 's', stopping further iteration.


for letter in 'lernpython':
    if letter == 'p':
        break

print('Current Letter :', letter)



# We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.

# the loop iterates over each letter in 'lernpython' but doesn't perform any operation, and after the loop finishes, the last letter ('n') is printed.

for letter in 'lernpython':
    pass
print('Last Letter :', letter)