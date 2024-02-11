import requests
import json

class SteamApiCaller:
  
    def __init__(self, key) -> None:
        self.key = key
        print(f"Key Loaded: {self.key}")

        with open('clean_app_list.json', encoding='utf8') as f:
            self.apps = json.load(f)

   
        

    def GameNameFromAppID(self, id: str):

        # Sometimes a game is no longer in the store but on profiles
        if id in self.apps:
            return self.apps[id]
        else:
            return "Missing From Store"
        

    def GetGamesFromUserID(self, id: str):
        
        # Get Request on the Steam Web API for a players ownee games
        url = f" http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.key}&steamid={id}&format=json"
        steam_response = requests.get(url)
        steam_json = steam_response.json()

        # Add Title to the entries
        response = {}
        games = []
        for entry in steam_json['response']['games']:
            game_entry = {'name': self.GameNameFromAppID(str(entry['appid'])), 'appid': entry['appid'], 'playtime_forever': entry['playtime_forever']}
            games.append(game_entry)
        

        # Build response
        response['games'] = games

        return response
