import easyocr

img = 'image.jpg'

reader = easyocr.Reader(['en']) #loading easy ocr model 
result = reader.readtext(img, detail = 0) #reading the image 

result_list = []

#appending extracted words into a list 
for word in result:
    result_list.append(word)

print(result_list)