# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)