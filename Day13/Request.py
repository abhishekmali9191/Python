# FTP File Transfer Protocol
# SMTP Simple Mail Transfer
# DNS Domain Name System
# SSH Secure Shell
# SOAP Simple Object Access
# HTTP Hyper Text Transfer
# HTTPS Hyper Text Transfer Secure
# HTTP Methods
# GET
# POST
# DELETE
# PUT
# PATCH
# HEAD
#
response = requests.get('https://restcountries.com/v3.1/all')

#check the status code
if response.status_code == 200:
    print("Resposnse recevied")
    print(response)
else:
    print("Failed to retrieve data", response.status_code)

countries = response.json()

for country in countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0]
    area = country.get('area', 'N/A')
    if name == 'India':
        print(f'Country: {name}')
        print(f'Capital: {capital}')
        print(f'Area: {area} sq km ')
        print(f"courency code : {country.get('currencies','N/A')}")
        print(f"region : {country.get('region')}")


# ############################################################
# OUTPUT
# Resposnse recevied
# <Response [200]>
# Country: India
# Capital: New Delhi
# Area: 3287590.0 sq km 
# courency code : {'INR': {'name': 'Indian rupee', 'symbol': '₹'}}
# region : Asia