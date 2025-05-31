from objects.OutputData import OutputData
from services.file_output_processor import FileOutputProcessor
import os

def file_output(data: OutputData):
    while True:
        print("Введіть шлях файлу для збереження результатів (наприклад, 'c:\\Users\\customer\\Documents'):")
        print("За умовчанням результат буде записано у 'output.csv' до ExampleOfCSVData/OutputDataCSV")
        file_path = input().strip()
        if not file_path:
            file_path = "ExampleOfCSVData/OutputDataCSV/output.csv"
        base, ext = os.path.splitext(file_path)
        counter = 1
        new_file_path = file_path
        while os.path.exists(new_file_path):
            new_file_path = f"{base}{counter}{ext}"
            counter += 1
        try:
            processor = FileOutputProcessor()
            processor.process(new_file_path, data)
            break
        except IOError as e:
            print(f"Помилка запису у файл: {e}")
            print("Спробуйте ще раз.")