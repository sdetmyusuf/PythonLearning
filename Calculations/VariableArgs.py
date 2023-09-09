def calTest(*args, **kwargs):
    print(args)
    for each_args in kwargs:
        print(each_args)
    for key, val in kwargs.items():
        print(key, val)


calTest(12, 34, name="yusuf", sal=23424243)


def cubeCal(x):
    return x ** 3


f = lambda x: "YES" if x % 2 == 0 else "NO"
print(f(4))

var = lambda x: x ** 3
print(var(5))

#passing two params to lambda
sum = lambda a, b: a + b
print(sum(2,4))

avg = lambda x, y, z: (x+y+z)/3
print(avg(1, 2, 3, ))

print(cubeCal(2))
