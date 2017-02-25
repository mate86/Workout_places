import os
from workout.build import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from workout.models import *

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , susp.py

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'workout.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('workout_places_SETTINGS', silent=True)


def init_db():
    workout_places = TableCreate()
    workout_places.connect_to_db()
    workout_places.drop_table()
    workout_places.create_tables()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_new_place', methods=['GET', 'POST'])
def add_new_place():
    if request.method == 'POST':
        district = request.form['district']
        address = request.form['address']
        place = request.form['place']
        description = request.form['description']

        new_place = WorkoutPlaces.create(
            district = district,
            address = address,
            place = place,
            description = description
        )
        return redirect(url_for('add_new_place'))
    return render_template('add_new_place.html')

@app.route('/finding_place')
def finding_place():
    places = WorkoutPlaces.select()
    return render_template('finding_place.html', places=places)
