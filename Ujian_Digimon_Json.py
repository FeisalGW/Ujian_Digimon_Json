import requests
from bs4 import BeautifulSoup
import json

#url
req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find('tbody')
data = data.find_all('tr')

#initiate list
dataDigimon = []

#get data from web & append to list
for x in data:
    no = x.find('td', width='5%').b.text.replace(u'\xa0', '')
    digimon = x.a.text
    img = x.img['src']
    stage = x.center.text
    type_ = x.find('td', width='7%').text
    attribute = x.find('td', width='7%').find_next_sibling().text
    memory = x.find('td', width='7%').find_next_sibling().find_next_sibling().text
    equip_slots = x.find('td', width='8%').text
    power = x.find_all('td', width=False)

    stats = []
    for item in power:
        stats.append(item.text)
    
    z = {
        "no": int(no),
        "digimon": digimon,
        "image": img,
        "stage": stage,
        "type": type_,
        "attribute": attribute,
        "memory": int(memory),
        "equip slots": int(equip_slots),
        "hp": int(stats[0]),
        "sp": int(stats[1]),
        "atk":int(stats[2]),
        "def":int(stats[3]),
        "int":int(stats[4]),
        "spd":int(stats[5])
        }
    dataDigimon.append(z)

#create json
with open('digimon.json', 'w') as dg:
    json.dump(dataDigimon, dg)