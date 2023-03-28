from flask import Flask, request, json
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():

    
    url = "https://instagram-scraper-2022.p.rapidapi.com/ig/following/"

    querystring = {"id_user":"44617448873"}

    headers = {
        "X-RapidAPI-Key": "02d25f21ecmsh6fd6238a435cabap1430c9jsna65bf3f1404e",
        "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()

    print(jsonData[next_max_id])

    return jsonData
