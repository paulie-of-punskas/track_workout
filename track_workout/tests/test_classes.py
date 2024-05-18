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

class TestExercise(unittest.TestCase):
    pratimai = exercises.exercises

    def test_exercise(self):
        with self.assertRaises(TypeError):
            Exercise("sikna", "", "", "", "")
            Exercise("sikna", "kelojimas", "", "", "")

        exer = Exercise("krutine", "spaudimas", "", "", "")
        self.assertIsInstance(exer, Exercise)
        
    
    print("krutine" in pratimai.keys())
    print("'muscle' value needs to be one of the following: " + str(list(pratimai.keys())))