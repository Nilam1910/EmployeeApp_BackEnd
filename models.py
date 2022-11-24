# import * means import everything from peewee

from peewee import *
import datetime
import os
from playhouse.db_url import connect
# DATABASE = SqliteDatabase('employees.sqlite')
# DATABASE = connect(os.environ.get('DATABASE_URL')
#                    or 'sqlite:///employees.sqlite')
if 'ON_HEROKU' in os.environ:  # later we will manually add this env var
    # in heroku so we can write this code
    DATABASE = connect(os.environ.get('DATABASE_URL'))  # heroku will add this
    # env var for you
    # when you provision the
    # Heroku Postgres Add-on
else:
    DATABASE = SqliteDatabase('employees.sqlite')

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
