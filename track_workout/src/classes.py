from datetime import datetime

class TotalWorkout:
    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%-d")

    def __str__(self):
        return f"TotalWorkout object created @ {self.date}"

class Exercise:
    def __init__(self, muscle, exercise, kg, rep):
        self.muscle = muscle
        self.exercise = exercise
        self.kg = kg
        self.rep = rep