import easyocr
import sys

sys.path.append("C:/Users/sayod/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/easyocr")

img = str(sys.argv[1])

reader = easyocr.Reader(['en']) #loading easy ocr model 
result = reader.readtext(img, detail = 0) #reading the image 

result_list = []

#appending extracted words into a list 
for word in result:
    result_list.append(word)

print(result_list)