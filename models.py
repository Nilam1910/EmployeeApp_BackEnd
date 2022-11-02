# import * means import everything from peewee

from peewee import *
import datetime

DATABASE = SqliteDatabase('employees.sqlite')

https: // docs.peewee-orm.com/en/latest/peewee/models.html  # field-types-table


class Employee(Model):
    name = CharField()
    admin = CharField()  # ForeignKeyField(Person, backref='employees')
    department = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Employee], safe=True)
    print("TABLES Created")
    DATABASE.close()
