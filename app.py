from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)

@app.route('/scraping/<id>', methods=["POST","GET"])
def scraping(id):

    nmi = request.args.get('nmi',  default = " ", type = str)

    if nmi != " ":
        querystring = {"id_user":""+id+"", "next_max_id":""+nmi+""}
    else:
        querystring = {"id_user":""+id+""}

    headers = {
        "X-RapidAPI-Key": "02d25f21ecmsh6fd6238a435cabap1430c9jsna65bf3f1404e",
        "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
    }

    url = "https://instagram-scraper-2022.p.rapidapi.com/ig/following/"

    

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    #return data

    return render_template('scraping.html', username=f'{id}', data=data)
