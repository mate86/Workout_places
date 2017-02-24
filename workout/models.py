from peewee import *


class Database():
    def __init__(self):
        self.lines = self.auth_inf_split(self.get_auth_inf('db_user.txt'))
        self.db = PostgresqlDatabase(self.lines[0], self.lines[1])

    def get_auth_inf(self, filename):
        with open(filename, "r") as file:
            line = file.readline()
        # setup connection string (and deleting the enter)
        line = line[:-1]
        line = str(line)
        return line

    def auth_inf_split(self, auth_inf):
        lines = auth_inf.split(', ')
        return lines

db = Database().db


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class WorkoutPlaces(BaseModel):
    district = CharField()
    street = CharField()
    place = CharField()
    description = CharField()
