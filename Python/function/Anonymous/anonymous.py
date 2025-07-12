# In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

def cube(x): return x*x*x   # without lambda

cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))