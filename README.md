App is used for tracking my workouts.

### How to run:
- start venv (`source venv/bin/activate`)
- in main directory, install (`pip install -e .`)
- edit and run `./scripts/save_workout.py`

### App usage:
- through web browser

### App pseudo diagram
- classes:
    - TotalWorkout (contains all exercises done on a particular day
    - Exercise (contains muscle groups, exercises, weights and repetitions done))
- extra data:
    - `static/exercises.py` - file contains all exercises
    - ~~WeightsReps (not sure if really needed)~~