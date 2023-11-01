import re
import urllib.request

str0 = "Master the fundamentals of Python while working on various usecases in easy steps"
str1 = "01-07-1988"
result = re.search(r'M\w{3}', str0)  # searching the substring which is having 3 chars after 'M'

result1 = re.findall(r'P\w{3}', str0)  # searching the substring which is having 3 chars after 'M'
result2 = re.findall(r'\d{2}-\d{2}-\d{4}', str1)
print(result.group())
print(result1)
print(result2)

# Checking regular expressions for special chars

result3 = re.search(r'^M\w*', str0)
result4 = re.search(r'M\w*', str0)
print(result3.group())
