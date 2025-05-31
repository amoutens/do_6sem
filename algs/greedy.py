from typing import List
from objects.InputData import InputData


def greedy_algorithm(input_data: InputData) -> List[List[int]]:
    x = []
    
    sorted_students = sorted(
        input_data.students.keys(), 
        key=lambda stud: input_data.students[stud], 
        reverse=True)

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
