from track_workout.src.classes import *
from track_workout.static import exercises
import unittest

# === create TotalWorkout class instance
class TestTotalWorkout(unittest.TestCase):
    def test_object_creation(self):
        workout = TotalWorkout()
        self.assertTrue(isinstance(workout, TotalWorkout))

    def test_return(self):
        workout = TotalWorkout()
        now = datetime.now().strftime("%Y-%m-%-d")
        test_string = "TotalWorkout object created @ " + str(now)
        self.assertEqual(workout.__str__(), test_string)

    def test_custom_date(self):
        date_string = "1990-03-11"
        workout = TotalWorkout(date_string)
        test_string = "TotalWorkout object created @ " + date_string
        self.assertEqual(workout.__str__(), test_string)     

    def test_to_list(self):
        geguze22 = [Exercise("nugara", "prisitraukimai", "", 4, ""),
                    Exercise("bicepsas", "curls - palms up", 3, 8, "")]
        
        total_workout = TotalWorkout("2024-05-22", geguze22)
        total_workout_list = total_workout.to_list()
        self.assertTrue(isinstance(total_workout_list, list))

class TestExercise(unittest.TestCase):
    pratimai = exercises.exercises

    def test_exercise(self):
        with self.assertRaises(TypeError):
            Exercise("sikna", "", "", "", "")
            Exercise("sikna", "kelojimas", "", "", "")

        exer = Exercise("krutine", "spaudimas", "", "", "")
        self.assertIsInstance(exer, Exercise)
        
    def test_exercise_and_totalworkout(self):
        geguze22 = [Exercise("nugara", "prisitraukimai", "", 4, ""),
                    Exercise("bicepsas", "curls - palms up", 3, 8, "")]
        
        total_workout = TotalWorkout("2024-05-22", geguze22)

        self.assertTrue(total_workout.date, "2024-05-22")
        self.assertEqual(total_workout.exercises_list[0].muscle, "nugara")
        self.assertEqual(total_workout.exercises_list[1].muscle, "bicepsas")

        with self.assertRaises(IndexError):
            total_workout.exercises_list[2]

    def test_to_list(self):
        exercise = Exercise("nugara", "prisitraukimai", "", 4, "")
        exercise_as_list = exercise.to_list()
        self.assertTrue(isinstance(exercise_as_list, list))
