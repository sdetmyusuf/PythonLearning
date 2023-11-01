Str = '''I love python
beacuse it supports multiple ways 
to store String'''

str3 = '''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''

str5 = '''I love python
beacuse it supports multiple ways 
to store String test'''

#[] double brackets are called the slice operators
#[:] it is called range opearator, the upper limit is always exclusive...
#slicing supports negative indices also.... which shows the position from end like -3 means third from last
str4 = "I love java"
print(str4[0:5])

print(str4[-4:])

print(str3)

# to revert the string use the syntax - [::-1]

print(str4[::-1])

str6 = "i live in delhi"
str6 =str6.capitalize()
#print(str6)

print(str6.count("i", 0, 15))

print(str6.casefold())