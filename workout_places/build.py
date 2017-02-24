# This script can create the database tables based on your models
from workout_places.models import *


class TableCreate():

    def __init__(self):
        self.db = db

    def connect_to_db(self):
        self.db.connect()

    def drop_table(self):
        self.db.drop_tables([WorkoutPlaces], safe=True)

    def create_tables(self):
        self.db.create_tables([WorkoutPlaces], safe=True)
