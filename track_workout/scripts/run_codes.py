from track_workout.src.classes import Exercise, TotalWorkout
from track_workout.scripts.save_workout import save_workout

# @ 22.05
# geguze22 = [Exercise("nugara", "prisitraukimai", "", 4, ""),
#             Exercise("nugara", "prisitraukimai", "", 3, ""),
#             Exercise("nugara", "prisitraukimai", "", 2, ""),
#             Exercise("nugara", "pulldown", 30, 8, ""),
#             Exercise("nugara", "pulldown", 30, 8, ""),
#             Exercise("nugara", "pulldown", 30, 8, ""),
#             Exercise("nugara", "row", 27.5, 8, ""),
#             Exercise("nugara", "row", 27.5, 8, ""),
#             Exercise("nugara", "row", 27.5, 8, ""),
#             Exercise("nugara", "shrugs", 15, 8, ""),
#             Exercise("nugara", "shrugs", 20, 8, ""),
#             Exercise("nugara", "shrugs", 20, 8, ""),
#             Exercise("bicepsas", "curls - preacher", 5, 8, ""),
#             Exercise("bicepsas", "curls - preacher", 6, 8, ""),
#             Exercise("bicepsas", "curls - preacher", 7, 8, ""),
#             Exercise("bicepsas", "curls - palms up", 3, 8, ""),
#             Exercise("bicepsas", "curls - palms up", 3, 8, ""),
#             Exercise("bicepsas", "curls - palms up", 3, 8, "")
# ]

geguze25 = [Exercise("krutine", "spaudimas", 37.5, 8, "masinos"),
            Exercise("krutine", "spaudimas", 37.5, 8, "masinos"),
            Exercise("krutine", "spaudimas", 37.5, 8, "masinos"),
            Exercise("krutine", "drugeliai", 32.5, 8, "masinos"),
            Exercise("krutine", "drugeliai", 35, 8, "masinos"),
            Exercise("krutine", "drugeliai", 35, 8, "masinos"),
            Exercise("krutine", "inclined bench press", 6, 8, "hanteliai"),
            Exercise("krutine", "inclined bench press", 6, 8, "hanteliai"),
            Exercise("krutine", "inclined bench press", 6, 8, "hanteliai"),
            Exercise("peciai", "spaudimas", 9, 8, "hanteliai"),
            Exercise("peciai", "spaudimas", 9, 8, "hanteliai"),
            Exercise("peciai", "spaudimas", 9, 6, "sunki serija"),
            Exercise("peciai", "spaudimas", 8, 2, "hanteliai"),
            Exercise("peciai", "sonai", 6, 8, "hanteliai"),
            Exercise("peciai", "sonai", 6, 8, "hanteliai"),
            Exercise("peciai", "sonai", 5, 8, "hanteliai"),
            Exercise("tricepsas", "skullcrushers", 2.5, 8, "stanga"),
            Exercise("tricepsas", "skullcrushers", 2.5, 8, "stanga"),
            Exercise("tricepsas", "skullcrushers", 2.5, 8, "stanga")
            ]

total_workout = TotalWorkout("2024-05-25", geguze25)
save_workout(total_workout.to_list(), total_workout.date)