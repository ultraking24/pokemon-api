import requests
poke_url = 'https://pokeapi.co/api/v2/pokemon/'

def get_poke(pokemon):
    endpoint = poke_url + pokemon
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        
        print(f"Pokemon Name: {data['name']}")
        print(f"Pokemon ID: {data['id']}")
        print(f"Pokemon Height: {data['height']}")
        print(f"Pokemon Weight: {data['weight']}")
        for poke_type in data["types"]:
            print(f'Pokemon type: {poke_type["type"]["name"]}')
        for poke_ability in data["abilities"]:
            print(f'Pokemon abilities: {poke_ability["ability"]["name"]}')


    except requests.RequestException as error:
        print(error)


pokemon = input("Enter a pokemon name.")
get_poke(pokemon)
