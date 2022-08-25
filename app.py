import os
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def status():
    return "{\"service\": \"sunrise-sunset\"}"

@app.route('/sunrise-sunset')
def sunrise_sunset():
    url = 'https://api.sunrise-sunset.org/json'
    lat = 50.08333
    lng = 14.46667
    return requests.get(url=url, params={'lat':lat, 'lng':lng}).json()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT',5000))
