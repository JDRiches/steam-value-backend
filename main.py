from fastapi import FastAPI  
from SteamAPICaller import SteamApiCaller

#Read in Secret Steam Key
f= open("keys.txt", "r")


api = SteamApiCaller(key=f.read())

app = FastAPI()   
@app.get("/") 
async def main_route():    
  return api.GetGamesFromID(id="76561198044048029")