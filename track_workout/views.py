from flask import Flask, render_template
from track_workout import app

import csv

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/view_workouts')
def view_workouts():
    with open("./track_workout/data/workouts.csv", newline="") as csv_file:
        workouts_file = csv.reader(csv_file, delimiter=",", quotechar="|")
        header = next(workouts_file)
        return render_template("view_workouts.html", header=header, rows=workouts_file)
