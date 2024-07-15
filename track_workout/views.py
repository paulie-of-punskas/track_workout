from flask import Flask, render_template, jsonify, request, send_file, redirect, url_for
from track_workout import app
from track_workout.static.exercises import exercises
from track_workout.src.classes import Exercise
from track_workout.scripts.save_workout import save_workout
from track_workout.scripts.db import db_connect, db_get_all_data, db_insert
import os
import csv
import json

# === set variables for uploading files
UPLOAD_FOLDER = str(os.path.dirname(os.path.realpath(__file__)) + "/data")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/view_workouts')
def view_workouts():
    with open("./track_workout/data/workouts.csv", newline="") as csv_file:
        workouts_file = csv.reader(csv_file, delimiter=",", quotechar="|")
        header = next(workouts_file)
        return render_template("view_workouts.html", header=header, rows=workouts_file)
    
@app.route('/view_workouts_sql')
def view_workouts_sql():
    workouts = db_get_all_data()
    col_names = ['date', 'muscle', 'exercise', 'kg', 'rep', 'comment']
    return render_template("view_workouts_sql.html", header=col_names, rows=workouts)

@app.route('/submit_workouts_sql')
def submit_workouts_sql():
    # === get keys for exercises dictionary
    muscle_groups = list(exercises)
    return render_template("submit_workouts_sql.html", muscle_groups=muscle_groups)

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
                        comment = frontend_data_json[4].get('comment'),
                        workout_date = frontend_data_json[5].get('workout_date'))

    # save_workout(exercise.to_list(), str(exercise.workout_date)) 
    workout_exercises :list = exercise.to_list()
    sql_string = f"'{workout_exercises[0]}', '{workout_exercises[1]}', '{workout_exercises[2]}', {workout_exercises[3]}, {workout_exercises[4]}, '{workout_exercises[5]}'"
    print(">> Following string will be used as value for db_insert()")
    print(sql_string)
    db_insert(sql_string)
    return jsonify(str("Data was received and saved."))

@app.route('/get_exercises/<muscle>')
def get_exercises(muscle):
    # === if selected muscle group is not found within exercises.py, return empty list
    # === else, return jsonified list, with exercises
    if muscle not in exercises:
        return jsonify([])
    else:
        return jsonify(exercises[muscle])

@app.route('/export_workouts')
def export_workout():
    """
    Export ./track_workout/data/workouts.csv file.
    """
    return send_file(str(UPLOAD_FOLDER + "/workouts.csv"), as_attachment=True)

@app.route("/import_workouts", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(UPLOAD_FOLDER + "/" + uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('upload_csv.html')
