import csv
from objects.InputData import InputData

class FileInputProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.raw_disciplines = []
        self.raw_students = []

    def __read_file(self):
        section = 'disciplines'
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row_num, row in enumerate(reader, 1):
                if not row or row[0].startswith('#'):
                    continue
                if row[0].strip().lower() == 'students':
                    section = 'students'
                    continue
                if section == 'disciplines':
                    if len(row) < 2:
                        print(f"Помилка у рядку {row_num}: недостатньо даних для дисципліни.")
                        continue
                    try:
                        capacity = int(row[1].strip())
                        if capacity < 1:
                            print(f"Помилка у рядку {row_num}: кількість місць повинна бути більше 0.")
                            continue
                        self.raw_disciplines.append(capacity)
                    except ValueError:
                        print(f"Помилка у рядку {row_num}: некоректна кількість місць '{row[1]}'.")
                elif section == 'students':
                    if len(row) < 3:
                        print(f"Помилка у рядку {row_num}: недостатньо даних для студента.")
                        continue
                    try:
                        idx = int(row[0].replace("Student", "").strip())
                        rating = int(row[1].strip())
                        wishlist = [int(x.strip()) for x in row[2:] if x.strip()]
                        if not wishlist:
                            print(f"Попередження у рядку {row_num}: студент без побажань.")
                        self.raw_students.append((idx, rating, wishlist))
                    except ValueError:
                        print(f"Помилка у рядку {row_num}: некоректний формат даних для студента.")

    def __preprocess(self):
        if not self.raw_disciplines:
            print("Помилка: не знайдено жодної дисципліни.")
        if not self.raw_students:
            print("Помилка: не знайдено жодного студента.")
        discipline_capacities = self.raw_disciplines
        students = {idx-1: rating for idx, rating, _ in self.raw_students}
        wishlists = {idx-1: wishlist for idx, _, wishlist in self.raw_students}

        for idx, wishlist in wishlists.items():
            for d in wishlist:
                if d < 0 or d >= len(discipline_capacities):
                    print(f"Попередження: студент {idx+1} має неіснуючий індекс дисципліни {d}.")
        return InputData(
            students=students,
            discipline_capacities=discipline_capacities,
            wishlists=wishlists,
        )
        
    def process(self):
        self.__read_file()
        return self.__preprocess()
