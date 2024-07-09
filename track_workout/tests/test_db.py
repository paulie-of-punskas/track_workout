from track_workout.src.classes import *
from track_workout.scripts import db
import unittest

class TestTotalWorkout(unittest.TestCase):
    def test_db_connection(self):
        db_connection = db.test_connection()
        column_names = ['date', 'muscle', 'exercise', 'kg', 'rep', 'comment']
        self.assertTrue(isinstance(db_connection, list))
        self.assertTrue(db_connection == column_names)
