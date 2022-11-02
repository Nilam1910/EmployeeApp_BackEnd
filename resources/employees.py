import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

# We can use this as a Python decorator for routing purposes
# first argument is blueprints name
# second argument is it's import_name
employee = Blueprint('employees', 'employee')
# https://www.tutorialspoint.com/flask/flask_request_object.htm
