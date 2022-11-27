
from flask import Flask, g, jsonify
from playhouse.db_url import connect
from flask_cors import CORS
import models
from resources.employees import employees
import os
from dotenv import load_dotenv
load_dotenv()  # takes the environment variables from .env
DEBUG = True
PORT = os.environ.get("PORT")

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)


CORS(employees, origins=['https://employee-app-nilam.herokuapp.com/', 'http://localhost:3000',
                         ], supports_credentials=True)  # authentication we need this supports_credentials
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


if os.environ.get('FLASK_DEBUG') != 'development':
    print('/non heroku')
    models.initialize()
# Run the app when the program starts!
#  initialize method in models folder
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
