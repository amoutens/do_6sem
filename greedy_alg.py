class GreedyAlgorithm:
    def __init__(self, m, n, W, Q, P):
        self.m = m
        self.n = n
        self.W = W
        self.Q = Q 
        self.P = P
        self.x = [[0 for _ in range(n)] for _ in range(m)]

    def greedy_algorithm(self):
        sorted_students = sorted(self.W.keys(), key=lambda s: self.W[s], reverse=True)

        for student in sorted_students:
            lfd = {'p': None, 'Q': -1}

            for discipline in self.P.get(student, []):
                if self.Q[discipline] > lfd['Q']:
                    lfd['p'] = discipline
                    lfd['Q'] = self.Q[discipline]

            if lfd['Q'] < 1:
                continue

            self.x[lfd['p']][student] = 1
            self.Q[lfd['p']] -= 1

        return self.x

    def print_matrix(self):
        for row in self.x:
            print(row)

    def calculate_objective_function(self):
        total = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.x[i][j] == 1:
                    total += self.W[j]
        return total
