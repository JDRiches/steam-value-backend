from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from src.SteamAPICaller import SteamApiCaller
from src.PriceAPICaller import PriceAPICaller
import os
import uvicorn

#Read in Secret Steam Key
if "STEAM_API_KEY" in os.environ:
    key = os.environ['STEAM_API_KEY']
else:
    with open("keys.txt", "r") as f:
        key = f.read()


if "PRICE_API_KEY" in os.environ:
    price_key = os.environ['PRICE_API_KEY']
else:
    with open("price_api_key.txt") as f:
        price_key = f.read()

steam_api = SteamApiCaller(key=key)
price_api = PriceAPICaller(key=price_key)

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# Path to get the games owend by user and time played
@app.get("/value/") 
async def games_route(user_id: str = "None"):
  
  steam_response = steam_api.GetGamesFromUserID(id=str(user_id))
  ids = price_api.AddCostToGames(steam_response['games'])

  

  return ids



if __name__ == "__main__":
    print("SOMEHITNG")
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))