import os
import requests
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<body>
<div>
<p id='currentPosition'></p>
<p id='positionName'>geoLocation</p>
</div>
<script>
    var x = document.getElementById('currentPosition');
    x.innerHTML = 'geoCoordinates'
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        x.innerHTML = 'Geolocation is not supported by this browser.';
      }
    }

    function showPosition(position) {
      x.innerHTML = 'Latitude: ' + position.coords.latitude +
      '<br>Longitude: ' + position.coords.longitude;

      var positionName = document.getElementById('positionName');
      let xhr = new XMLHttpRequest();
      xhr.open('GET', '/nominatim?lat=' + position.coords.latitude + '&lon=' + position.coords.longitude);
      xhr.send();
      xhr.onload = () => {positionName.innerHTML =  xhr.responseText;
        }
    }
    getLocation();

</script>
</body>
</html>
    '''

@app.route('/sunrise-sunset')
def sunrise_sunset():
    url = 'https://api.sunrise-sunset.org/json'
    lat=request.args['lat']
    lon=request.args['lon']
    resp = Response(requests.get(url=url, params={'lat':lat, 'lng':lon}).content)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    return resp

@app.route('/nominatim-reverse')
def nominatimReverse():
    url = 'https://nominatim.openstreetmap.org/reverse'
    lat=request.args['lat']
    lon=request.args['lon']
    resp = Response()requests.get(url=url, params={'format': 'jsonv2', 'lat':lat, 'lon':lon}).content)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT',5000))
