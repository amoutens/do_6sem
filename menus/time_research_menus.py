from algs.greedy import greedy_algorithm
from services.generated_input_processor import GeneratedInputProcessor
import time


def research_time_on_disciplines_menu():
    n = 0
    while True:
        print("Введіть кількість студентів (одне ціле число):")
        input_str = input()
        try:
            n = int(input_str)
            if n <= 1:
                print("Кількість студентів повинна бути більше 1.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")

    n_lower = 60
    n_upper = 100
    l_percentage = 0.5
    
    times = 0
    while True:
        print("Введіть кількість досліджень (одне ціле число):")
        input_str = input()
        try:
            times = int(input_str)
            if times <= 0:
                print("Кількість досліджень повинна бути більше 0.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
        
    inputs = []
    for m in range(times):
        l = 1 if m * l_percentage == 0 else m * l_percentage
        inputs.append(GeneratedInputProcessor(n, n_lower, n_upper, m, l).process())
        
    greedy_outputs = []
    for input_data in inputs:
        start_time = time.time()
        result = greedy_algorithm(input_data)
        elapsed_time = time.time() - start_time
        greedy_outputs.append(elapsed_time)
        
    gale_shapley_outputs = []
    for input_data in inputs:
        start_time = time.time()
        result = gale_shapley_outputs(input_data)
        elapsed_time = time.time() - start_time
        greedy_outputs.append(elapsed_time)
        
    return greedy_outputs, gale_shapley_outputs

def research_time_on_students_menu():
    n_lower = 60
    n_upper = 100
    m = []
    while True:
        print("Введіть кількість дисциплін (одне ціле число):")
        input_str = input()
        try:
            m = int(input_str)
            if m <= 1:
                print("Кількість дисциплін повинна бути більше 1.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")

    l = []
    while True:
        print(
            "Введіть максимальну кількість бажаних дисциплін для кожного студента (одне ціле число):"
        )
        input_str = input()
        try:
            l = int(input_str)
            if l <= 1:
                print("Кількість бажаних дисциплін повинна бути більше 1.")
                continue
            if l > m:
                print(
                    "Кількість бажаних дисциплін не повинна бути більше кількості дисциплін."
                )
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
    
    times = 0
    while True:
        print("Введіть кількість досліджень (одне ціле число):")
        input_str = input()
        try:
            times = int(input_str)
            if times <= 0:
                print("Кількість досліджень повинна бути більше 0.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
        
    inputs = []
    for n in range(times):
        inputs.append(GeneratedInputProcessor(n, n_lower, n_upper, m, l).process())
        
    greedy_outputs = []
    for input_data in inputs:
        start_time = time.time()
        result = greedy_algorithm(input_data)
        elapsed_time = time.time() - start_time
        greedy_outputs.append(elapsed_time)
        
    gale_shapley_outputs = []
    for input_data in inputs:
        start_time = time.time()
        result = gale_shapley_outputs(input_data)
        elapsed_time = time.time() - start_time
        greedy_outputs.append(elapsed_time)
        
    return greedy_outputs, gale_shapley_outputs