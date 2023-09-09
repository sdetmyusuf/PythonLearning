def test(fun):
    def innertest():
        result = fun()
        return result + 2

    return innertest


def num():
    return 5


result = test(num)


# print(result())


# here we are applying the decorator test to this function
@test
def newnum():
    return 2


print(newnum())
print("==============================================")


def stringAdd(fun):
    def inner(str):
        result = fun(str)
        result = result + "????????"
        return result

    return inner


def stringdecor(fun):
    def inner(str):
        res = fun(str)
        res = res + "How are you?????"
        return res

    return inner


@stringAdd
@stringdecor
def hello(name):
    return "hello!!! " + name + " "


print(hello("Yusuf"))

print("===============decorator chaining, we can apply more than one decorator to a single function")
