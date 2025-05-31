import random

from objects.InputData import InputData


class GeneratedInputProcessor:
    def __init__(self, n, n_lower, n_upper, m, l):
        self.n = n
        self.n_lower = n_lower
        self.n_upper = n_upper
        self.m = m
        self.l = l

    def process(self):
        students = [random.randint(self.n_lower, self.n_upper) for _ in range(self.n)]

        discipline_capacities = [0 for _ in range(self.m)]
        for _ in range(int(self.n * 1.25)):
            discipline_capacities[random.randint(0, self.m - 1)] += 1

        wishlists = [random.sample(range(self.m), random.randint(1, self.l)) for _ in range(self.n)]
        return InputData(students, discipline_capacities, wishlists)