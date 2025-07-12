# Python Functions is a block of statements that does a specific task.

# The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

# def function_name(parameter):
#     #statement
#     return function_name


def fun():
    print("Welcome to GFG")
fun()

# Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

def evenOdd(x: int) ->str:
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


#default arguments
def myFun(x, y):
    print("x: ", x)
    print("y: ", y)


myFun(10,20)