String = "The cat is on the catlog. The cat is also in the category"
pattern = r'\scat\s'
print(re.findall(pattern, String))

##[' cat ', ' cat ']