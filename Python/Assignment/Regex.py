# python 2
import re

fileDemo = 'regex_sum_42.txt'
fileActual = 'regex_sum_248261.txt'

file = open(fileActual)
text = file.read()
strNumber = re.findall('[0-9]+', text)
digitalNumber = list(map(int, strNumber))
result = sum(digitalNumber)
print result
