import requests
import json

def fetch_country_data(is_country):
    count_url = "https://api.first.org/data/v1/countries"
    response = requests.get(count_url)

    countries = response.json()["data"]

    user_code = input('Enter the country code you want: ').strip()

    result = {}

    for key, value in countries.items():
        if is_country:
            print(key,value)
            result[key] = value
        else:
            if key == user_code:
                print(key, value)
                result[key] = value
                break
    else:
        if not result:
            print('country code not found')
        return
    
    with open('country_data.json', 'w') as file:
         json.dump(result,file, indent=4) #standard way to write json data to file
        

    print("\nData successfully saved to country_data.json")

#country_name = input('ente country name: ')
is_country = False
fetch_country_data(is_country)