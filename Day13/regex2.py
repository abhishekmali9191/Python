import re
string = "Hello my birth date is 08/09/2024 and today is 16/09/2024 and 12312/04/200a21 "
pattern = r'[0-3][0-9]/[0-1][0-9]/\d{2,4}'
# pattern = r'^(:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(:0[1-9]|1[0-2])/(:2[0-9][0-9][0-9])'
# pattern = r'^(?:19|20)\d\d/(?:0[1-9]|1[0-2])/(?:0[1-9]|[12][0-9]|3[01])$'
pattern = r'\s[\d][\d]/[\d][\d]/[\d][\d][\d][\d]\s'
print(re.findall(pattern,string))

###[' 08/09/2024 ', ' 16/09/2024 ']