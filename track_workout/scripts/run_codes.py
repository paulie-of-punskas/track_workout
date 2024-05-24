from track_workout.src.classes import Exercise, TotalWorkout
from track_workout.scripts.save_workout import save_workout

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
save_workout(total_workout.to_list())