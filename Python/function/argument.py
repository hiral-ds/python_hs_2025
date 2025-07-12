# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

def myFun(x, y):
    print("x: ", x)
    print("y: ", y)


myFun(10,30)


# Keyword Arguments allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

def student(fname, lname):
    print(fname, lname)

student(fname='function', lname='Practice')
student(lname='Practice', fname='python')


# We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")