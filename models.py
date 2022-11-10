# import * means import everything from peewee

from peewee import *
import datetime

DATABASE = SqliteDatabase('employees.sqlite')
# DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///employees.sqlite')

# https: // docs.peewee-orm.com/en/latest/peewee/models.html  # field-types-table


class Employee(Model):
    name = CharField()
    admin = CharField()  # ForeignKeyField(Person, backref='employees')
    department = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    # safe true will create the table only if they are not existed
    DATABASE.create_tables([Employee], safe=True)
    print("Connected to the DB and created tables if they don't already exist")
    DATABASE.close()
