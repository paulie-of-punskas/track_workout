from track_workout.src.classes import *
import csv
import os.path

def save_workout(exercise, workout_date):
    """
    Method takes TotalWorkout object as input and saves it to csv file.
    """
    if os.path.isfile("./track_workout/data/workouts.csv") == True:
        with open("./track_workout/data/workouts.csv", 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(exercise)
    else:
        with open("./track_workout/data/workouts.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["date", "muscle", "exercise", "kg", "rep", "comment"])
            writer.writerow(exercise)
    print(">> New data was added for " + str(workout_date))
