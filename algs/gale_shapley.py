from typing import List
from objects.InputData import InputData


def gale_shapley_algorithm(input_data: InputData) -> List[List[int]]:
    m = len(input_data.discipline_capacities)
    n = len(input_data.students)

    x = [[0 for _ in range(n)] for _ in range(m)]
    H = {i: [] for i in range(m)}
    overflow = [False for _ in range(m)]

    wishlists = {i: list(input_data.wishlists[i]) for i in range(len(input_data.students))}
    queue = list(range(len(input_data.students)))

    while queue:
        student = queue.pop(0)

        if not wishlists[student]:
            continue

        d = wishlists[student][0]

        H[d].append(student)
        H[d].sort(key=lambda s: input_data.students[s], reverse=True)

        if overflow[d] or len(H[d]) > input_data.discipline_capacities[d]:
            last = H[d].pop()
            queue.append(last)
            overflow[d] = True

        wishlists[student].pop(0)

    for d in range(m):
        for student in H[d]:
            x[d][student] = 1

    return x
