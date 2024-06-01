App is used for tracking my workouts.

### How to run without Flask:
- start venv (`source venv/bin/activate`)
- in main directory, install (`pip install -e .`)
- edit and run `./scripts/save_workout.py`

### Running Flask app:
as per: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
- `export FLASK_APP=track_workout`
- `pip install -e .`
- `flask run -h localhost -p 5001`

### App usage:
- through web browser

### App pseudo diagram
- classes:
    - TotalWorkout (contains all exercises done on a particular day
    - Exercise (contains muscle groups, exercises, weights and repetitions done))
- extra data:
    - `static/exercises.py` - file contains all exercises
    - ~~WeightsReps (not sure if really needed)~~

### Stack:
- backend: Python and Flask
- frontend: HTML, JS, AJAX (https://stackoverflow.com/a/44654011)