from typing import List
from objects.InputData import InputData


def greedy_algorithm(input_data: InputData) -> List[List[int]]:
    x = [[0 for _ in range(len(input_data.students))] for _ in range(len(input_data.discipline_capacities))]
    
    sorted_students = sorted(
        range(len(input_data.students)),  
        key=lambda i: input_data.students[i],
        reverse=True
    )

    for student in sorted_students:
        lfd = {'p': None, 'Q': 0}

        for discipline in input_data.wishlists[student]:
            if input_data.discipline_capacities[discipline] > lfd['Q']:
                lfd['p'] = discipline
                lfd['Q'] = input_data.discipline_capacities[discipline]

        if lfd['Q'] < 1:
            continue

        x[lfd['p']][student] = 1
        input_data.discipline_capacities[lfd['p']] -= 1

    return x
