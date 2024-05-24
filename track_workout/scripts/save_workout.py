from track_workout.src.classes import *
import csv
import os.path

def save_workout(workout):
    """
    Method takes TotalWorkout object as input and saves it to csv file.s
    """
    if os.path.isfile("./track_workout/data/workouts.csv") == True:
        with open("./track_workout/data/workouts.csv", 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(workout)
    else:
        with open("./track_workout/data/workouts.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(workout)
    return "New data was added."


# print("len = ", len(geguze22))
# total_workout_str = []

# for j in range(len(geguze22)):
#     # print(total_workout.exercises_list[j])
#     object = total_workout.exercises_list[j]
#     xx = [object.muscle + "," + object.exercise + "," + str(object.kg) + "," + str(object.rep) + "," + object.comment]
#     total_workout_str.append(xx)

# def save_workout():
#     if os.path.isfile("./track_workout/data/scraped_data.csv") == True:
#         with open("./track_workout/data/scraped_data.csv", 'a', newline='') as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerows(scraped_data)
#     else:
#         with open("./track_workout/data/scraped_data.csv", 'w', newline='') as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerows(scraped_data)
#     return "New data was scraped."