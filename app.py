# https: // flask.palletsprojects.com/en/2.2.x/quickstart/

from flask import Flask, g
from flask_cors import CORS
import models
from resources.employees import employees
import os
# from playhouse.db_url import connect
DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)


CORS(employees, origins=['http://localhost:3000'], supports_credentials=True)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

app.register_blueprint(employees, url_prefix='/api/v1/employees')
# sets up the directions for handling the routes for the api(employee)
# The default URL ends in / ("my-website.com/").


@app.before_request
def before_request():
    """Connect to the database before each request."""
    print('you should see this before each request')
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    print('you should see this after each request')
    g.db = models.DATABASE
    g.db.close()
    return response


if os.environ.get('FLASK_ENV') != 'development':
    print('/non heroku')
    models.initialize()
# Run the app when the program starts!
#  initialize method in models folder
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
