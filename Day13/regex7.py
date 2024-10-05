password = "Abhishek@123"
pattern = r'^[a-zA-Z]\S{4,10}\d$'
if re.search(pattern,password):
    print("Valid")
else:
    print("Invalid")
    
    
    
    # Valid