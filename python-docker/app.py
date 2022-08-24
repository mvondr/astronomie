import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == 'main'
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
