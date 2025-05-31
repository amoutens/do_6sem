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
            for row in reader:
                if not row or row[0].startswith('#'):
                    continue
                if row[0].strip().lower() == 'students':
                    section = 'students'
                    continue
                if section == 'disciplines':
                    self.raw_disciplines.append(int(row[1].strip()))
                elif section == 'students':
                    idx = int(row[0].replace("Student", "").strip())
                    rating = int(row[1].strip())
                    wishlist = [int(x.strip()) for x in row[2:] if x.strip()]
                    self.raw_students.append((idx, rating, wishlist))

    def __preprocess(self):
        discipline_capacities = self.raw_disciplines
        students = {idx-1: rating for idx, rating, _ in self.raw_students}
        wishlists = {idx-1: wishlist for idx, _, wishlist in self.raw_students}
        return InputData(
            students=students,
            discipline_capacities=discipline_capacities,
            wishlists=wishlists,
        )
        
    def process(self):
        self.__read_file()
        return self.__preprocess()
