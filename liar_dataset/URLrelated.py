#pip install beautifulsoup4
#pip install google

from show import *
from googlesearch import search 
    

with open('headline.txt','r') as file:
    url = file.read()

fb = "https://www.facebook.com"
for i in search(url, tld="co.in", num=10, start=1, stop=5, pause=2.0):
    if fb in i:
        continue
    print("<a href=\"" + i + "\">" + i + "</a><br>")