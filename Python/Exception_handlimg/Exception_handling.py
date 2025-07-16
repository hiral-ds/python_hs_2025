try:
    a=0
    b=100/a
    
except ZeroDivisionError:
    print("Zero division error")
else:
    print("Enter value ",b)
finally:
    print("execution completed")
    
