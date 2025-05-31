from objects.InputData import InputData


def manual_input():
        students = []
        while True:
            print("Перелічіть рейтинги студентів (Формат - ##, #, ..., ##; # - Цифра):")
            input_str = input()
            try:
                students = [int(s.strip()) for s in input_str.split(',')]
                break
            except ValueError:
                print("Некоректний ввід. Спробуйте ще раз.")
        
        discipline_capacities = []
        while True:
            print("Перелічіть кількість місць на кожній дисципліні (Формат - ##, #, ..., ###; # - Цифра):")
            input_str = input()
            try:
                discipline_capacities = [int(s.strip()) for s in input_str.split(',')]
                break
            except ValueError:
                print("Некоректний ввід. Спробуйте ще раз.")
                
        wishlists = []
        for stud_id, _ in enumerate(students):
            while True:
                print(f"Перелічіть побажання студента №{stud_id + 1}")
                print("(Формат - ##, #, ..., ##; # - Цифра, побажання не можуть півторюватись та бути більше ніж дисциплін):")
                input_str = input()
                try:
                    whishlist = [int(s.strip()) for s in input_str.split(',')]
                    if any(w > len(discipline_capacities) for w in whishlist):
                        print("Некоректний ввід. Побажання не можуть бути більше ніж кількість дисциплін.")
                        continue
                    if len(whishlist) != len(set(whishlist)):
                        print("Некоректний ввід. Побажання не можуть півторюватись.")
                        continue
                    wishlists.append([int(s.strip()) for s in input_str.split(',')])
                    break
                except ValueError:
                    print("Некоректний ввід. Спробуйте ще раз.")
        
        return InputData(students, discipline_capacities, wishlists)