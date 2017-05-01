from flask import Flask, make_response
import os

DEBUG = not int(os.environ['FLASK_PRODUCTION'])
PORT = int(os.environ['PORT'])

app = Flask(__name__)

@app.route('/')
def index():
    return 'CS-Unplugged Render Engine'

@app.route('/_ah/health')
def health_check():
    content = ''
    response = make_response(content, 200)
    return response

if __name__ == '__main__':
    print(DEBUG, PORT)
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
