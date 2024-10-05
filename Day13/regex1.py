#  create a file which has multiple urls along with other text data. Extract only urls from the file

import re

def extract_urls(filename):
  urls = []
  with open(urlFile, 'r') as file:
    for line in file:
      # Use regular expression to find URLs
      found_urls = re.findall(r'https?://[^\s]+', line)
      if found_urls:
        urls.append(found_urls)
  return urls

# Example usage
urlFile = '/content/sample_data/urls.txt'  # Replace with your file name
extracted_urls = extract_urls(urlFile)
print(extracted_urls)
# # Regular expression in python
# uses re library
# re.search():searches for the firsst match
# re.match(): checks for a match only at


# use of meta-characters


