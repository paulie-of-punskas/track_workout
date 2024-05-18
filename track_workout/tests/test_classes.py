from track_workout.src.classes import *
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
