# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)