from datetime import datetime
from track_workout.static import exercises

class TotalWorkout:
    """
    TotalWorkout class contains all exercises ("Exercise" class instances), that were done
    in during workout session. If no workout date is provided, then it assigns current date
    as its value.
    date - date of workout
    exercises_list - list containing objects of Exercise class
    """
    # === "overloaded" constructor, for custom workout entries
    def __init__(self, date=None, exercises_list=[]):
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%-d")
        else:
            self.date = date
        self.exercises_list = exercises_list

    def to_list(self):
        exercises_list_str = []
        for exercise in self.exercises_list:
            exercise_with_date = exercise.to_list()
            # exercise_with_date.append(self.date)
            exercise_with_date.insert(0, self.date)
            exercises_list_str.append(exercise_with_date)
        return exercises_list_str

    def __str__(self):
        return f"TotalWorkout object created @ {self.date}"
    

class Exercise:
    """
    """
    def __init__(self, muscle, exercise, kg, rep, comment):
        self.muscle = muscle
        self.exercise = exercise
        self.kg = kg
        self.rep = rep
        self.comment = comment

    @property
    def muscle(self):
        print(">> Getter used for 'muscle' property")
        return self._muscle
    
    @muscle.setter
    def muscle(self, value):
        print(">> Setter used for 'muscle' property")
        muscle_groups = exercises.exercises.keys()
        if not value in muscle_groups:
            raise TypeError("'muscle' value needs to be one of the following: " + str(muscle_groups))
        self._muscle = value

    @property
    def exercise(self):
        print(">> Getter used for 'exercise' property")
        return self._exercise
    
    @exercise.setter
    def exercise(self, value):
        # === get exercises for given muscle group
        user_muscle = self._muscle
        print(">> Setter used for 'exercise' property, muscle = " + user_muscle)
        pratimai = exercises.exercises
        user_muscle_exercises = list(pratimai[user_muscle])
        if not value in user_muscle_exercises:
            raise TypeError("'exercise' value needs to be one of the following " + str(user_muscle_exercises))
        # print(">> exercises for " + user_muscle + ": " + str(user_muscle_exercises))
        self._exercise = value
    
    def to_list(self):
        return [str(self.muscle), str(self.exercise), str(self.kg), str(self.rep), str(self.comment)]

    # def __str__(self):
    #     xx = self.muscle + "," + self.exercise + "," + str(self.kg) + "," + str(self.rep) + "," + self.comment
    #     return xx
