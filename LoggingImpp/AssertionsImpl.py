try:
    num = int(input("Enter a number"))
    assert num%2==0, "You have incorrect result not divisible by 2"
except AssertionError as obj:
    print(obj)

print("After assertion")