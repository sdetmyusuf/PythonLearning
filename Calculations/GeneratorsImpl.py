def cusGene(x, y):
    while x < y:
        yield x
        x = x + 1


result = cusGene(10, 20)
for i in result:
    print(i)
print("===============keywords in python=======================")

