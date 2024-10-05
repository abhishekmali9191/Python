string1 = "Error: File not founs.\n Warning:Low disk space \nError: Access Denied."
pattern = r'^Error.*\.$'
print(re.findall(pattern,string1, re.MULTILINE))

# ['Error: File not founs.', 'Error: Access Denied.']