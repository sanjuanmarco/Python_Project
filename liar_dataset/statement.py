import sys
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')

from svm import inputPredict
from googlesearch import search
import requests

state = str(sys.argv[1])

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
  
    for i in search(state, tld="co.in", num=5, start=0, stop=4, pause=2):
        if fb in i or mfb in i:
            continue
        print("<a href=\"" + i + "\">" + i + "</a><br>")



