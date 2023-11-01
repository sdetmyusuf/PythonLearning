import re
import urllib.request

sites = ["google.com", "bing.com"]

for s in sites:
    print("visiting ", s)
    response = urllib.request.urlopen("http://"+s)
    text = response.read()
    result = re.findall("<title>.*</title>", str(text), re.I)
    print(result[0])
