import requests
from pprint import pprint

url = f'https://akabab.github.io/superhero-api/api/all.json'
info = requests.get(url).json()
super_man = []
super = 0
for n in info:
    if n['name'] == 'Hulk' or n['name'] == 'Captain America' or n['name'] == 'Thanos':
        super_man.append({'name':  n['name'], 'intelligence': n['powerstats']['intelligence']})
for key in super_man:
    if super < int(key['intelligence']):
        super = int(key['intelligence'])
        name = key['name']
print(f'Самый умный супергерой: {name} \nЕго интеллект: {super}')