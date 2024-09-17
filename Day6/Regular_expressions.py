# Regeular Expression
import re
result = re.findall(r'a.b','aab acb a#b adb ab a\nb zab and')
print(result)

result1 = re.findall(r'^Hello','Hello world! Hi World')
print(result1)

result2 = re.findall(r'World$','Hello World')
print(result2)

result3 = re.findall(r'ca*t','ct cat caat caaat cacacat')
print(result3)

result4 = re.findall(r'go+','go goo gooo goooo tgoot')
print(result4)

result5 = re.findall(r'colou?r','color colour colouur')
print(result5)

result6 = re.findall(r'a{2,4}','a aa aaa aaaa aaaa aaaa aaaa')
print(result6)

result7 = re.findall(r'[aeiou]','mumbai pune delhi')
print(result7)

result8 = re.findall(r'dog|cat','I have a dog and a cat and a dog')
print(result8)