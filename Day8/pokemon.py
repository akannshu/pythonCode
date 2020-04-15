import requests
import json

def get_pokemon_data(name="pikachu"):
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

pokemon_name = input("Enter the Pokemon's Name : ")
x = get_pokemon_data(pokemon_name)
# print(x['cards'])

# import matplotlib.pyplot as plt

# r = requests.get(x["cards"][1]["imageUrl"], stream=True)
# with open('./001.png', 'wb') as f:
#     for chuck in r.iter_content(1024):
#         f.write(chuck)

# image_data = plt.imread('./001.png')
# plt.imshow(image_data) 
# plt.show()       

import urllib.request
import matplotlib.pyplot as plt

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

urllib.request.urlretrieve(x['cards'][1]['imageUrl'], "00000001.png")

image_data = plt.imread('./00000001.png')
plt.imshow(image_data) 
plt.show()       

