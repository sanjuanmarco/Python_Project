import sys
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')


import requests #pip3 install request
import trafilatura #pip3 install trafilatura
import nltk
from rake_nltk import Rake
from lxml import html
from newsplease import NewsPlease #pip3 install news-please
from show import *


url = str(sys.argv[1])

#url = "https://twitter.com/rkkaaay/status/1449462065995960323"

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
    if head != None:
        print("Headline: " + head)
    else:
        print("Statement: " + result)

    read_dataframe('test.csv')
    accuracy(head)
    #rake algo
    #r = Rake()
    #words = r.extract_keywords_from_text(result)

    # contains keywords
    #f_words = r.get_ranked_phrases()[0:20] #20 related phrases

    # functions for accuracy and label
    
    

except requests.ConnectionError as exception:
    print("URL does not exist, please make sure to provide a valid URL.")

except Exception:
    print("Twitter")



