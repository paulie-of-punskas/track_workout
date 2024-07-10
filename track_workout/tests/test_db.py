from track_workout.src.classes import *
from track_workout.scripts import db
import unittest
import pyodbc

class TestTotalWorkout(unittest.TestCase):
    
    def test_db_connection(self):
        db_connection = db.db_connect()
        print(db_connection)
        column_names = ['date', 'muscle', 'exercise', 'kg', 'rep', 'comment']
        self.assertTrue((db_connection is not None))
        # self.assertTrue(isinstance(db_connection, Cursor))

    def test_conn(self):
        connection_string :str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_pass};Connection Timeout=60;Encrypt=yes;TrustServerCertificate=no'
        with connection_string as conn:
            with conn.cursor() as cursor:
                rows = []
                cursor.execute("SELECT * from track_workout")
                # row = cursor.fetchall()
                row = cursor.fetchall()
                print(row[0])
                