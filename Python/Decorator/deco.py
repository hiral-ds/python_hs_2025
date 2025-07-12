# Defination : Decorator is a function that takes another function as argument and retuns a function.

def greet():
    def demo():
        print("Good Morning")
        
        print("Thhanks for using this function.")
    # return demo
    demo()

# @greet
def fun():
    print("Hello world")

fun()
greet()
# greet(fun)()

print("-"*70)


def decorator(fun):
    def wrapper():
        print("Transaction inited...")
        fun()
        print("Transaction Completed...")
    return wrapper

@decorator
def hello():
    print("....Executing all steps of Transaction....")

hello()

# decorator(hello)()