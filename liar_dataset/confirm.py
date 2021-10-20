from show import *

with open('statement.txt','r') as file:
    text = file.read()
print("<b>Statement: </b>" + text)

read_dataframe('test.csv')
accuracy(text)
