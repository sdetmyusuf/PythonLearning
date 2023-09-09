from functools import reduce
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x:x%2==0, lst))
print(even)
for i in even:
    print(i)

#using map function
double  = list(map(lambda n:n*2, lst))
print(double)
for i in  double:
    print(i)

#using reduce function
val = list(reduce(lambda x,y:x+y, lst))
