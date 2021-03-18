import requests
from bs4 import BeautifulSoup
import json

URL="https://bulbapedia.bulbagarden.net/w/index.php?title=List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
poke_content = soup.find(id='mw-content-text')
poke_tables=poke_content.find_all('table')

pokemonGenerations = poke_tables[1:9]
i = 1

pokeJSON = []

for generationTable in pokemonGenerations:
    pokeGenerationJSON = []
    for dataCount in range(3, len(generationTable), 2):
        row = generationTable.contents[dataCount]
        kdex = row.contents[1].text.strip()
        ndex = row.contents[3].text.strip()
        name = row.contents[7].text.strip()
        type1 = row.contents[9].text.strip()
        type2 = ''
        if len(row.contents) > 10:
            type2 = row.contents[11].text.strip()
        types=[type1,type2]
        pokeURL = 'https://bulbapedia.bulbagarden.net/wiki/{0}_(Pokémon)'.format(name)
        # print(kdex,ndex,name,types,pokeURL)
        pokeGenerationJSON.append({
            'kdex': kdex,
            'ndex': ndex,
            'name': name,
            'types': types,
            'URL': pokeURL
        })
    
    pokeJSON.append({
        'generation' : i,
        'pokemons' : pokeGenerationJSON
    })
    i += 1

with open('pokemon.json', 'w', encoding='utf-8') as f:
    json.dump(pokeJSON, f, ensure_ascii=False, indent=4)

