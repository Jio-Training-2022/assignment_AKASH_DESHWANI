# Find all the urls in a data in a file 

import re

with open('Code\scripts\data.txt', 'r') as f:
    data = f.read()
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)
    print(urls)
