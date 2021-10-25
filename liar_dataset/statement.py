import sys
from show import *

state = str(sys.argv[1])

f = open("statement.txt", "w")
f.write(state)
f.close()

with open('statement.txt','r') as file:
    text = file.read()
print(r"<b>Statement: </b>" + text)

read_dataframe('test.csv')
accuracy(text)
