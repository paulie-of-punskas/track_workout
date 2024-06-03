from flask import Flask, render_template, jsonify
from track_workout import app
from track_workout.static.exercises import exercises
import csv
from requests import request

@app.route('/index')
@app.route('/')
def index():
    return 'Labas.'

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
    return render_template("submit_workouts.html", muscle_groups=muscle_groups)

@app.route('/ingest', methods=['POST'])
def ingest_js():
    # === get data from submit_workouts and create instance object 
    post_request = request.args.get('post')
    pass

@app.route('/get_exercises/<muscle>')
def get_exercises(muscle):
    # === if selected muscle group is not found within exercises.py, return empty list
    # === else, return jsonified list, with exercises
    if muscle not in exercises:
        return jsonify([])
    else:
        return jsonify(exercises[muscle])
