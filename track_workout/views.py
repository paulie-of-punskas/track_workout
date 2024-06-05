from flask import Flask, render_template, jsonify, request
from track_workout import app
from track_workout.static.exercises import exercises
from track_workout.src.classes import Exercise, TotalWorkout
import csv
import json


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

@app.route('/ingest_js', methods=['POST'])
def ingest_js():
    # === get JSON data from submit_workouts and create instance object
    frontend_data_json = request.get_json()
    print(frontend_data_json)
    exercise = Exercise(muscle = frontend_data_json[0].get('muscle'), 
                        exercise = frontend_data_json[1].get('exercise'), 
                        kg = frontend_data_json[2].get('kg'), 
                        rep = frontend_data_json[3].get('rep'), 
                        comment = frontend_data_json[4].get('comment'))
    return jsonify(str("Data was received and saved."))

@app.route('/get_exercises/<muscle>')
def get_exercises(muscle):
    # === if selected muscle group is not found within exercises.py, return empty list
    # === else, return jsonified list, with exercises
    if muscle not in exercises:
        return jsonify([])
    else:
        return jsonify(exercises[muscle])
