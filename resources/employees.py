import models

# (we can use the * if we wants but that can slowdown the porcess and in python we just use what we need)
from flask import Blueprint,  request, jsonify

from playhouse.shortcuts import model_to_dict

# We can use this as a Python decorator for routing purposes
# first argument is blueprints name
# second argument is it's import_name
employees = Blueprint('employees', 'employees')
# https://www.tutorialspoint.com/flask/flask_request_object.htm
# BluePrints - The basic concept of blueprints is that they record operations to execute when registered on an application.# INDEX ROUTE ["GET"]

# INDEX ROUTE, methods=['GET']


# @employees.route('/') # by default this is a get route but can specify in following
# def employees_index():
#     return "employees resource working"  # worked
@employees.route('/', methods=['GET'])
def employees_index():
    all_employees = models.Employee.select()
    print('result of employee select')
    print(all_employees)
    employee_dicts = []
    for employee in all_employees:
        employee_dict = model_to_dict(employee)
        employee_dicts.append(employee_dict)  # make sure it only dict
    return jsonify({  # too see our object print beautifully
        'data': employee_dicts,
        'message': f"Successfully 🎉 found {len(employee_dicts)}employees",
        'status': 200
    }), 200


# # CREATE ROUTE, methods=["POST"]


@employees.route('/', methods=["POST"])  # worked
def create_employees():
    # see request payload anagolous to req.body in express
    payload = request.get_json()
    print(payload)
    # print(type(payload), 'payload')
    # employee = models.Employee.create(**payload)
    new_employee = models.Employee.create(
        name=payload['name'], admin=payload['admin'], department=payload['department'])  # need this one frontend
    print(dir(new_employee))
    # --------------------------------------------------for frontend
    employee_dict = model_to_dict(new_employee)
    # return jsonify(data=employee_dict, status={"code": 201, "message": "Success"}) # or
    return jsonify(data=employee_dict, message='Successfully created employee!!! 🎉', status=201), 201


# SHOW ROUTE, '<id>', methods=['GET']


@employees.route('<id>', methods=['GET'])
def get_one_employee(id):
    employee = models.Employee.get_by_id(id)
    print(employee)
    return jsonify(
        data=model_to_dict(employee),
        message='Success!!! 🎉',
        status=200
    ), 200

# UPDATE ROUTE, '/<id>', methods=['PUT'] ### (edit_route or View_route)


@employees.route('/<id>', methods=['PUT'])  # worked
def update_employee(id):
    # what ever we get from this we wants to assign to employee
    payload = request.get_json()
    # so we need to located the model before we need to do anything with it
    # (**payload)it a spread operator for all of this  name=payload['name'], admin=payload['admin'], department=payload['department']) # (in javascript is ...)
    query = models.Employee.update(**payload).where(models.Employee.id == id)
    # https://docs.peewee-orm.com/en/latest/peewee/querying.html
    query.execute()
    # row = query.execute()
    # print(row) to see row been updated
    return jsonify(
        data=model_to_dict(models.Employee.get_by_id(id)),
        status=200,
        message='resource updated successfully 🎉'
    ), 200

# DELETE,  '/<id>',methods=['DELETE']


@employees.route('/<id>', methods=['DELETE'])
def delete_employee(id):
    query = models.Employee.delete().where(models.Employee.id == id)
    query.execute()
    return jsonify(
        data='resource successfully deleted',
        status=200,
        message='resource successfully deleted'
    ), 200
# To check all Employee crated


# @employees.route('/', methods=["GET"])
# def get_all_employees():
#     # find the employees and change each one to a dictionary into a new array
#     try:
#         employees = [model_to_dict(employee)  # model_to_dict(employee) - is a function that will change Model object (employee) to a Dictionary class, because to jsonify something from a "Model" class. To respond to client we must change our datatype
#                      for employee in models.Dog.select()]
#         print(employees)
#         return jsonify(data=employees, status={"code": 200, "message": "Success"})
#     except models.DoesNotExist:
#         # CREATE ROUTE ["POST"]
#         return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


# inside create route print diff ways new_employee data before # employee_dict = model_to_dict(new_employee)
    # print(new_employee)  # will print the ID and we can check the data in sqlite3
    # # see the object
    # # this one can give us better info. and dict is a class attribute
    # print(employee.__dict__)
    # # Look at all the methods
    # # this one allow us to look everything come with the model's class and attributes
    # print(dir(new_employee))
    # # we cannot jsonify because new employee just run onces so that is where our playhouse shortcuts models to disc come in
    # # to convert the ... wait for it ...model to dict
    # print(model_to_dict(employee), 'model to dict')
