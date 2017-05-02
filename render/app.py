from flask import Flask, make_response
from QueueHandler import QueueHandler
import os

DEBUG = not int(os.environ['FLASK_PRODUCTION'])
PORT = int(os.environ['PORT'])

app = Flask(__name__)

@app.route('/')
def index():
    return 'CS-Unplugged Render Engine'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route('/_ah/health')
def health_check():
    content = ''
    response = make_response(content, 200)
    return response

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
