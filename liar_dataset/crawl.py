import sys
# sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
# sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
# sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
# sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
# sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
# sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')

sys.path.append(r'F:/Programming Files/Python/Python Project/venv/Lib/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/win32')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/pythonwin')

import requests #pip3 install request
import trafilatura #pip3 install trafilatura
import nltk
from rake_nltk import Rake
from lxml import html
from newsplease import NewsPlease #pip3 install news-please
from show import *


url = str(sys.argv[1])

try:
    response = requests.get(url)
    download = trafilatura.fetch_url(url)
    res = trafilatura.extract(download, include_comments=False, 
        include_tables=False, no_fallback=True, output_format='xml')

    a = str(res)

    part = a.partition("h2") #remove strings in h2
    output = part[0]

    mytree = html.fromstring(output) #transforming xml to string
    result = str(trafilatura.process_record(mytree))
    #print(result) #prints main content

    #get news title
    article = NewsPlease.from_url(url)
    head = article.title

    twitter = "https://twitter.com"
    fb = "https://www.facebook.com"
    if head != None:
        print("<b>URL: </b>" + url)
        print("<br><b>Headline:</b> " + head)
        read_dataframe('test.csv')
        accuracy(head)

        f = open("headline.txt", "w")
        f.write(head)
        f.close()

    elif twitter in url or fb in url:
        print("Sorry, social media links cannot be accessed due to privacy laws.<br>")
        print("For social media posts, please copy the statement and paste in the corresponding field.")

    else:
        f = open("statement.txt", "w")
        f.write(head)
        f.close()

    
    

except requests.ConnectionError as exception:
    print("URL does not exist, please make sure to provide a valid URL.")

except Exception:
    print("")



