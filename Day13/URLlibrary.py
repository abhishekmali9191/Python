# URL library : Standard library in python used for working with urls
# provides modeules and functions to
# Fetch data from urls
# Handle url encoding
# Decode urls
# Manage requests and response over http and https protocols
from urllib.parse import urlparse, parse_qs, urlencode

# Extracting the domain name fro a full url to identify which website is being accessed
url = "https://www.example.com/search?query=python&sort=recent"
parsed_url = urlparse(url)
domain_name = parsed_url.netloc
print(f'Domain :{domain_name}')
print(f'Path : {parsed_url.path}')
print(f'Query : {parsed_url.query}')

# Extracting or modifying query parameters in a url, at runtime
url = "https://www.example.com/search?query=python&sort=recent"
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
print(f'Query Params : {query_params}')

# Adding or removing query parameters from an existing url
base_url = 'https://www.example.com/search'
query_params = {
    'query': 'python',
    'sort': 'recent'
}
updated_url = base_url + '?' + urlencode(query_params)
print(f'Updated URL : {updated_url}')


# ##############################################################
# OUTPUT
# Domain :www.example.com
# Path : /search
# Query : query=python&sort=recent
# Query Params : {'query': ['python'], 'sort': ['recent']}
# Updated URL : https://www.example.com/search?query=python&sort=recent