try:
    
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    
    print("Division by 0 not accepted")
else:
    
    print("Division = ", z)
finally:
    print("We have performed the operation")
    


try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of  range")
else:
    print(x, "is within the  range")

