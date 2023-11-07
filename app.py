from flask import Flask, request, json, render_template
import requests
from instagrapi import Client

app = Flask(__name__)

cl = Client()

cl.login("ernestigler","OkOx9GHJKL*7*")


@app.route('/scraping/<id>', methods=["POST","GET"])
def scraping(id):

    nmi = request.args.get('nmi',  default = " ", type = str)

    if nmi != " ":
        querystring = {"id_user":""+id+"", "next_max_id":""+nmi+""}
    else:
        querystring = {"id_user":""+id+""}

    headers = {
        "X-RapidAPI-Key": "f2923eedf0msh2990d552a2003d3p12f51bjsn663c397ea72b",
        "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
    }

    url = "https://instagram-scraper-2022.p.rapidapi.com/ig/followers/"

    

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    #return data

    return render_template('scraping.html', username=f'{id}', data=data)

@app.route('/ig')
def ig():
    user_id = cl.user_id_from_username(ernestigler)

    print(user_id)

    return {}