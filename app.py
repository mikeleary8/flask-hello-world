from flask import Flask, request, json, render_template
import requests

app = Flask(__name__)


@app.route('/retreat-webhook', methods=["POST"])
def retreat_webhook(token):

    body = request.json

    print(body)

    return body, 200