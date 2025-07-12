# array is a collection of items stored at contiguous memory locations.
# Unlike Python lists (can store elements of mixed types), arrays must have all elements of same type. Having only homogeneous elements makes it memory-efficient.

import array as arr

# creating array of integers
a = arr.array('i', [1, 2, 3])   #The 'i' is a type code that specifies the type of elements the array will hold.

print(a[0])

# a.append(5)
# print(a)

# 'i' stands for signed integer (usually 4 bytes = 32 bits).
# It means the array will contain standard integer values