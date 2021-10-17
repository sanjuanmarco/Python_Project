import sys

sys.path.append('C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.9_3.9.2032.0_x64__qbz5n2kfra8p0/lib/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/win32/lib')
sys.path.append('C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/Pythonwin')
sys.path.append("C:/Users/Kyle/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/easyocr")

import easyocr

img = sys.argv[1]


reader = easyocr.Reader(['en'], gpu=False, model_storage_directory='C:/Users/Kyle/.EasyOCR/model', user_network_directory='C:/Users/Kyle/.EasyOCR/user_network')
result = reader.readtext(img, detail = 0) #reading the image 

result_list = []

#appending extracted words into a list 
for word in result:
    result_list.append(word)

#Concatenation of list
sentences = " ".join(result_list)
print(sentences)
