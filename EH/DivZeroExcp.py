try:
    a,b = [int(x) for x in input("Enter the numbers").split()]
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Denominator should not be zero")

