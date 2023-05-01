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
url = "https://api-football-v1.p.rapidapi.com/v3/standings"

querystring = {"season": "2022", "team": "78"}

headers = {
    "X-RapidAPI-Key": "bfb3b963dbmshf426ee149a36421p169c18jsne042794f929f",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
placement = data.get('response')[0].get(
    'league').get('standings')[0][0].get('rank')
points = data.get('response')[0].get(
    'league').get('standings')[0][0].get('points')
championnat = data.get('response')[0].get(
    'league').get('standings')[0][0].get('group')

# Get current date
date = datetime.now().strftime("%d/%m/%Y")


# Send a tweet
response = client.create_tweet(text="A la date du " + date + " les @girondins sont " +
                               str(placement) + "ème de " + championnat + " avec " + str(points) + " points. #FCGB")

print(response)
