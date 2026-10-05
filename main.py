#handles api calling
import requests
poke_url = 'https://pokeapi.co/api/v2/pokemon/'

def get_poke(pokemon):
    endpoint = poke_url + pokemon
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        return data
    


    except requests.RequestException as error:
        print(error)
        return None



