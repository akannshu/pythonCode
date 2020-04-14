import requests

url = "https://sv443.net/jokeapi/category/Programming?blacklistFlags=political"

response = requests.get(url)

#print(response)
recieved_data = response.json()

# print(r)

for data in recieved_data.keys():
    if data != 'warning' and data != 'id':
        print("{} : {}".format(data, recieved_data[data]))
