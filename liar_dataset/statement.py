import sys
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')

import requests #pip3 install requests
import trafilatura #pip3 install trafilatura
from rake_nltk import Rake
from similarity import *
from lxml import html
from svm import inputPredict
from googlesearch import search
import requests
import warnings

warnings.filterwarnings("ignore")

state = str(sys.argv[1])

r = Rake()
r.extract_keywords_from_text(state)
r.get_ranked_phrases()
result = listToString(r.get_ranked_phrases())

try:
    response = requests.get(state)
    print("<b>URL detected, use the corresponding field for url inputs.</b> stringmanip <label>")
    print("<label>No related links</label>")

except requests.ConnectionError as exception:
    inputPredict(state)
    print("stringmanip " + state)

    print("<label><label>Related links</label>")


    fb = "https://www.facebook.com"
  
    for i in search(state, tld="co.in", num=5, start=0, stop=4, pause=2):
        if fb in i:
            continue
        print("<a href=\"" + i + "\">" + i + "</a><br>")

except Exception:
    inputPredict(state)
    words = state.replace("\"", "&#39;").replace("\'", "&quot;")
    print("stringmanip " + words)

    print("<label><label>Related links</label>")


    fb = "https://www.facebook.com"
    mfb = "https://m.facebook.com"
    url_article = []
    x = 0
    for i in search(state, tld="co.in", num=5, start=0, stop=4, pause=2):
        url_content = ""
        url_article.append(i)
        if fb in i or mfb in i:
            continue

        download = trafilatura.fetch_url(url_article[x])
        res = trafilatura.extract(download, include_comments=False, 
        include_tables=False, no_fallback=True, output_format='xml')
        
        a = str(res)
        part = a.partition("h2") #remove strings in h2
        output = part[0]
        mytree = html.fromstring(output) #transforming xml to string
        url_content = str(trafilatura.process_record(mytree)) #prints main content
        r1 = Rake()
        r1.extract_keywords_from_text(url_content)
        r1.get_ranked_phrases()
        url_content = listToString(r1.get_ranked_phrases())
        similarity_score =float("{:.5f}".format(cosine_sim(result,url_content)))
           

        print("<a href=\"" + i + "\">" + i + "</a>", similarity_score * 100 ,r"% similarity score","<br>")
   
        x = x + 1


