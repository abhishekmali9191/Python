String = "My phone 123 number 456 is 123-456-7890123454321 124 "
pattern = r'\d'
digit = re.findall(pattern, String)
set1 = set(digit)
dict1 = {i:digit.count(i) for i in set1}
print(dict1)
# print(tuple(i for i in dict1.items() if dict1.values()==3))
pattern1 = r'\s[\d][\d][\d]\s'
print(re.findall(pattern1,String))



# {'2': 5, '7': 1, '6': 2, '3': 4, '5': 3, '4': 5, '9': 1, '0': 1, '1': 5, '8': 1}
# [' 123 ', ' 456 ', ' 124 ']