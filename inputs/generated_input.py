from objects.InputData import InputData
import random


def generated_input():
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
            
    n_lower = 0
    n_upper = 0
    while True:
        print("Введіть межі по оцінкам студентів (пара цілих чисел через зап'яту, перше <= друге):")
        input_str = input()
        try:
            n_lower_str, n_upper_str = input_str.split(',')
            n_lower = int(n_lower_str.strip())
            n_upper = int(n_upper_str.strip())
            if n_lower > n_upper:
                print("Перше число повинно бути менше або дорівнювати другому.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
    
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
        print("Введіть максимальну кількість бажаних дисциплін для кожного студента (одне ціле число):")
        input_str = input()
        try:
            l = int(input_str)
            if l <= 1:
                print("Кількість бажаних дисциплін повинна бути більше 1.")
                continue
            if l > m:
                print("Кількість бажаних дисциплін не повинна бути більше кількості дисциплін.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")            
    
    students = [random.randint(n_lower, n_upper) for _ in range(n)]

    discipline_capacities = [0 for _ in range(m)]
    for _ in range(int(n * 1.25)):
        discipline_capacities[random.randint(0, m - 1)] += 1

    wishlists = [random.sample(range(m), random.randint(1, l)) for _ in range(n)]

    return InputData(students, discipline_capacities, wishlists)