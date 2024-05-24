from track_workout.src.classes import *
import csv
import os.path

def save_workout():
    pass

# @ 22.05
geguze22 = [Exercise("nugara", "prisitraukimai", "", 4, ""),
            Exercise("nugara", "prisitraukimai", "", 3, ""),
            Exercise("nugara", "prisitraukimai", "", 2, ""),
            Exercise("nugara", "pulldown", 30, 8, ""),
            Exercise("nugara", "pulldown", 30, 8, ""),
            Exercise("nugara", "pulldown", 30, 8, ""),
            Exercise("nugara", "row", 27.5, 8, ""),
            Exercise("nugara", "row", 27.5, 8, ""),
            Exercise("nugara", "row", 27.5, 8, ""),
            Exercise("nugara", "shrugs", 15, 8, ""),
            Exercise("nugara", "shrugs", 20, 8, ""),
            Exercise("nugara", "shrugs", 20, 8, ""),
            Exercise("bicepsas", "curls - preacher", 5, 8, ""),
            Exercise("bicepsas", "curls - preacher", 6, 8, ""),
            Exercise("bicepsas", "curls - preacher", 7, 8, ""),
            Exercise("bicepsas", "curls - palms up", 3, 8, ""),
            Exercise("bicepsas", "curls - palms up", 3, 8, ""),
            Exercise("bicepsas", "curls - palms up", 3, 8, "")
]

total_workout = TotalWorkout("2024-05-22", geguze22)

print("")
print(total_workout.to_list())

print(type(total_workout.to_list()))

# print("len = ", len(geguze22))
# total_workout_str = []

# for j in range(len(geguze22)):
#     # print(total_workout.exercises_list[j])
#     object = total_workout.exercises_list[j]
#     xx = [object.muscle + "," + object.exercise + "," + str(object.kg) + "," + str(object.rep) + "," + object.comment]
#     total_workout_str.append(xx)

# === save data to csv file
# print(total_workout_str)

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