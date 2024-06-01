from flask import Flask, render_template, jsonify
from track_workout import app
from track_workout.static.exercises import exercises
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

@app.route('/submit_workouts')
def submit_workouts():
    # === get keys for exercises dictionary
    muscle_groups = list(exercises)
    # === workaround to add empty cell, so that dropdown list has 
    muscle_groups.append("-- Select")
    return render_template("submit_workouts.html", muscle_groups=muscle_groups)
    # === get values for exercises dictionary

@app.route('/get_exercises/<muscle>')
def get_exercises(muscle):
    if muscle not in exercises:
        return jsonify([])
    else:
        return jsonify(exercises[muscle])
