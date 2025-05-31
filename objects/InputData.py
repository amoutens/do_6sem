import copy

class InputData:
    def __init__(self, students, discipline_capacities, wishlists):
        self.students = students
        self.discipline_capacities = discipline_capacities
        self.wishlists = wishlists
        
    def copy(self):
        return InputData(
            copy.deepcopy(self.students),
            copy.deepcopy(self.discipline_capacities),
            copy.deepcopy(self.wishlists)
        )
