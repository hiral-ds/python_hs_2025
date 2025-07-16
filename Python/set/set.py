# Sets are used to store multiple items in a single variable.

# A set is a collection which is mutable, unordered, and unindexed.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
