import re


def checkPattern():
    s = "take up an idea. an idea at a time"
    result = re.search(r'a\w', s)
    print(result.group())

def checkPatternList():
    s = "take up an idea. an idea at a time"
    result = re.findall(r'a\w\w'
                        r'', s)
    print(result)



checkPatternList()

