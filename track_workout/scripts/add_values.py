from track_workout.scripts.db import db_insert, db_get_all_data

import csv
# === read csv into environment
with open("/Users/pb/Downloads/workouts_2024Jul10.csv", newline="") as csv_file:
    workouts_file = csv.reader(csv_file, delimiter=",", quotechar="|")
    for row in workouts_file:
        if row[0] == "2024-07-10":
            sql_string = f"'{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}'"
            print(sql_string)
