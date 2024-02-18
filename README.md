# Steam Value Backend

## 📖 Project Overview

Ever wondered how much value for money you've gotten out of games you bought from Steam? Well now you can!
This API gathers the amount of minutes you've played on a game and the price the game currently is.

## 🌐 Other APIs Used

### Steam Web API
Used for getting the game librarys of users.

### Is There Any Deal API (IsThereAnyDeal.com)
Used for getting the prices of games the user has in thier library.

## 📡 Running The API

Ran using uvicorn.
```
python -m uvicorn src.main:app --host=0.0.0.0 --port=8080
```

For a local container run use
```
docker run -e STEAM_API_KEY=**** -e PRICE_API_KEY=**** -p 8080:8080 my-api
```
It is important to use ```-p 8080:8080``` to be able to access the app.

## 🔧 Infrastructure

Infrastructure hosted on the Google Cloud Platform.

- Images are pushed to Googles Aritfact Registry.
- Images in the GAR are then deployed to and ran in a Cloud Run Service
