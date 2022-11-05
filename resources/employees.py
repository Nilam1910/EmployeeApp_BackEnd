import models

from flask import Blueprint, jsonify, request #(we can use the * if we wants but that can slowdown the porcess and in python we just use what we need)

from playhouse.shortcuts import model_to_dict

# We can use this as a Python decorator for routing purposes
# first argument is blueprints name
# second argument is it's import_name
employees = Blueprint('employees', 'employee')
# https://www.tutorialspoint.com/flask/flask_request_object.htm
# BluePrints - The basic concept of blueprints is that they record operations to execute when registered on an application.# INDEX ROUTE ["GET"]

# INDEX ROUTE
@employees.route('/')
def employees_index():
   return "employees resource working"

#
@employees.route('/', methods=["GET"])
def get_all_employees():
    # find the employees and change each one to a dictionary into a new array
    try:
        employees = [model_to_dict(employee)  # model_to_dict(employee) - is a function that will change Model object (employee) to a Dictionary class, because to jsonify something from a "Model" class. To respond to client we must change our datatype
                     for employee in models.Dog.select()]
        print(employees)
        return jsonify(data=employees, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})# CREATE ROUTE ["POST"]

# CREATE ROUTE
@employees.route('/', methods=["POST"])
def create_employees():
    # see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    employee = models.Employee.create(**payload)
    # see the object
    print(employee.__dict__)
    # Look at all the methods
    print(dir(employee))
    # Change the model to a dict
    print(model_to_dict(employee), 'model to dict')
    employee_dict = model_to_dict(employee)
    return jsonify(data=employee_dict, status={"code": 201, "message": "Success"})