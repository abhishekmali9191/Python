# Hands on GET Method
try:
    #count = 0
    userRegion = input("Enter Region : ").capitalize()
    userCode = input("Enter Currency code : ").upper()
    response = requests.get('https://restcountries.com/v3.1/all')
    countries = response.json()
    for country in countries:
        region = country.get('region',{})
        currency_code=  country.get('currencies',{})

        if region == userRegion and tuple(currency_code.keys())[0] == userCode:
            # count += 1
            # print(country)
            print(f"Country : {country.get('name',{}).get('common', 'N/A')}")
            print(f"Capital : {country.get('capital', ['N/A'])[0]}")
            print(f"Area : {country.get('area', 'N/A')} sq km")
            print(f'Currency Code : {tuple(currency_code.keys())[0]}')
            print(f'Region : {region}')
            break
    else:
        raise Exception("Not found")
except Exception as e:
    print(e)

# ########################################################################
# OUTPUT
# Enter Region : Asia
# Enter Currency code : INR
# Country : India
# Capital : New Delhi
# Area : 3287590.0 sq km
# Currency Code : INR
# Region : Asia