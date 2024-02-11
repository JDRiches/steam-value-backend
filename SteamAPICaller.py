import requests

class SteamApiCaller:
  
    def __init__(self, key) -> None:
        self.key = key
        print(f"Key Loaded: {self.key}")


    def GetGamesFromID(self, id: str):
        url = f" http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.key}&steamid={id}&format=json"

        response = requests.get(url)

        response_json = response.json()

        return response_json
