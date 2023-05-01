import tweepy
import requests
from datetime import datetime
from time import strftime

# Authenticate to Twitter account "Classement FCGB"
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAAMUmwEAAAAADtCXFyyY1%2B91b7syKf0hkIGTXdw%3DhlfMbKcMUv79FZocuOnkASC6t6NziFjXNavsFWPnAztyqX8EYp',
                       consumer_key='qBrxFN7psNom471W6wbizcOei', consumer_secret='nAU4AD2AEoP6MzhWQETzohNh7R2xz8J4zNlvv0QSO0IHlWeokJ',
                       access_token='1647638812518932481-sFVgjF1g0aYbET5IyimvdQE0EIenCA', access_token_secret='6ox1g1JXvS3WRKNraJaEB165vIpfVSdi8qykoghc9Htom',
                       )

# import Bordeaux data from API
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"season":"2022","team":"78","last":"1","status":"FT"}

headers = {
    "X-RapidAPI-Key": "bfb3b963dbmshf426ee149a36421p169c18jsne042794f929f",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
home = data.get('response')[0].get('teams').get('home').get('name')
ext = data.get('response')[0].get('teams').get('away').get('name')
scoreHome = data.get('response')[0].get('goals').get('home')
scoreExt = data.get('response')[0].get('goals').get('away')
numJ = data.get('response')[0].get('league').get('round').split("-")[1].strip()
dateMatch = data.get('response')[0].get('fixture').get('date').split("T")[0]
winnerAway = data.get('response')[0].get('teams').get('away').get('winner')
winnerHome = data.get('response')[0].get('teams').get('home').get('winner')

# Get current date
date = datetime.now().strftime("%Y-%m-%d")

if (home == "Bordeaux"):
    if (winnerHome == True):
        response = client.create_tweet(text="Les @girondins ont gagné " + str(scoreHome) + " - " + str(scoreExt) + " contre " + ext + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")
    elif (winnerHome == "null" and winnerAway == "null"):
        response = client.create_tweet(text="Les @girondins ont fait match nul " + str(scoreHome) + " - " + str(scoreExt) + " contre " + ext + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")
    else:
        response = client.create_tweet(text="Les @girondins ont perdu " + str(scoreHome) + " - " + str(scoreExt) + " contre " + home + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")
elif (ext == "Bordeaux"):
    if (winnerAway == True):
        response = client.create_tweet(text="Les @girondins ont gagné " + str(scoreExt) + " - " + str(scoreHome) + " contre " + home + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")
    elif (winnerHome == "null" and winnerAway == "null"):
        response = client.create_tweet(text="Les @girondins ont fait match nul " + str(scoreExt) + " - " + str(scoreHome) + " contre " + home + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")
    else:
        response = client.create_tweet(text="Les @girondins ont perdu " + str(scoreExt) + " - " + str(scoreHome) + " contre " + home + " lors de la " + numJ + "ème journée de Ligue 2. #FCGB")

print(response)