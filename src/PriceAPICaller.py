import requests
import json

class PriceAPICaller:
    
    def __init__(self, key: str) -> None:
        
        self.key = key


    def AddCostToGames(self, games: list):

        payload = []
        for game in games:
            payload.append(f"app/{game['appid']}")

        url = f"https://api.isthereanydeal.com/unstable/id-lookup/game/v1"

        id_response = requests.post(url, data=json.dumps(payload))
        response = id_response.json()

        #Adding on the price api id
        for game in games:
            game['id'] = response[f"app/{game['appid']}"]

        payload = []

        for game in games:
            payload.append(game['id'])

        url = f"https://api.isthereanydeal.com/games/overview/v2?key={self.key}&country=GB&shops=61"

        price_response = requests.post(url, data=json.dumps(payload))
        response = price_response.json()

        # Create price dict
        price_dict = {}

        for price in response['prices']:
            price_dict[price['id']] = price['current']['price']['amount']

        for game in games:
            try:
                game['price'] = price_dict[game['id']]
            except:
                game['price'] = -1

        return games