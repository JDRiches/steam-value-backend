from fastapi import FastAPI  
from SteamAPICaller import SteamApiCaller
import os
import uvicorn

#Read in Secret Steam Key
if "STEAM_API_KEY" in os.environ:
    key = os.environ['STEAM_API_KEY']
else:
    f = open("keys.txt", "r")
    key = f.read()

api = SteamApiCaller(key=key)

app = FastAPI()

# Path to get the games owend by user and time played
@app.get("/games/{user_id}") 
async def games_route(user_id):    
  return api.GetGamesFromUserID(id=str(user_id))



if __name__ == "__main__":
    print("SOMEHITNG")
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))