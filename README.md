# clonehero-chart-generator
Turn any song on Spotify into a playable Clone Hero format!
## Setup
1. Create a spotify developer dashboard https://developer.spotify.com/dashboard/login (this gives us access to spotify API)
2. Add ```localhost:8080``` as your redirect uri in your spotify developer dashboard
3. You will need to add the ```client-id``` and ```client-secret``` into their respective enverionment variables in ```/backend/Dockerfile```

## How to Run
1. Navigate to the root folder
2. run ```docker-compose build --no-cache```
3. run ```docker-compose up```
4. Navigate to ```localhost:8080```
5. Once downloaded, unzip the file, and move the songs to your clone hero songs folder

## Clone Hero
1. Navigate to Settings/General
2. Scan Songs
3. Find them in Quickplay
