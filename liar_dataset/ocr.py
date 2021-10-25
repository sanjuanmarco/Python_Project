import sys
import easyocr
#sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')
#sys.path.append('C:/Users/Kyle/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
#sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
#sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
#sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
#sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
#sys.path.append("C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/easyocr")

sys.path.append(r'F:/Programming Files/Python/Python Project/venv/Lib/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/win32')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/pythonwin')
sys.path.append("C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/easyocr")



import easyocr
from svm import inputPredict
from googlesearch import search 

img = sys.argv[1]


reader = easyocr.Reader(['en'], gpu=False, model_storage_directory='C:/Users/jake/AppData/Roaming/Python/Python39/site-packages/easyocr/model', user_network_directory='C:/Users/Kyle/.EasyOCR/user_network')
result = reader.readtext(img, detail = 0) #reading the image 

result_list = []

#appending extracted words into a list 
for word in result:
    result_list.append(word)

#Concatenation of list
sentences = " ".join(result_list)

if (not sentences):
    print("<b>For accurate results, use high quality images. Results will be based on image clarity. Kindly double check if the produced statement is correct and the same as what is on the image.</b>")
    print("stringmanip ")
else:
    print("<b>For accurate results, use high quality images. Results will be based on image clarity. Kindly double check if the produced statement is correct and the same as what is on the image.</b><br>")
    inputPredict(sentences)
    print("stringmanip " + sentences)

    print("<label><label>Related links</label>")


    fb = "https://www.facebook.com"
    bm = "https://b-m.facebook.com"
    mfb = "https://m.facebook.com"
  
    for i in search(sentences, tld="co.in", num=5, start=0, stop=4, pause=2):
        if fb in i or bm in i or mfb in i:
            continue
        print("<a href=\"" + i + "\">" + i + "</a><br>")








