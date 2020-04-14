import requests

url = "https://currencyapi.net/api/v1/rates?key=jWj8yXpic2OrRAlhc2DJzz29jUNESzFYQ3gP"


response = requests.get(url)

recieved_data = response.json()

for data in recieved_data.keys():
    if data == "rates":
        rates = recieved_data[data]
        for rateData in rates:
            if rateData == "INR":
                print(f'{rateData} : {rates[rateData]}')
