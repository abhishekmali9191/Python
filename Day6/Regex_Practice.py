result = re.findall(r'start .* end','Hello start day with lecture and it goes up to the  end Byebye')
print(result)


# output  ['start day with lecture and it goes up to the  end']
#----------------------------------------------------------------

sss = "This is an example sentence with several words such as apple, eaglbd, or night. Note that words like orange and upturn fit the criteria, but not applepie."
print(re.findall(r'\b[aeiou]\w*[bcdfghjklmnpqrstvwxyz]\b', sss))

# output  ['is', 'an', 'as', 'eaglbd', 'or', 'and', 'upturn']
#----------------------------------------------------------------

sss = "This is an example sentence 2with several words 1such as apple, eagle, or night. Note 4that words like orange 56and upturn fit the criteria, but not applepie."
print(re.findall(r'\b[0-9]\w*[a-zA-Z]', sss))

# output   ['2with', '1such', '4that', '56and']
#----------------------------------------------------------------

result = re.findall(r'Note .* !','Note Hello start day with lecture and it goes up to the ! end Byebye')
print(result)



# output  ['Note Hello start day with lecture and it goes up to the !']