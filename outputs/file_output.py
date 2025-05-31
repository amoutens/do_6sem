from objects.OutputData import OutputData
from services.file_output_processor import FileOutputProcessor


def file_output(data: OutputData):
    while True:
        print("Введіть шлях файлу для збереження результатів (наприклад, 'c:\\Users\\customer\\Documents'):")
        file_path = input().strip()
        try:
            processor = FileOutputProcessor(file_path, data)
            processor.process()
            break
        except IOError as e:
            print(f"Помилка запису у файл: {e}")
            print("Спробуйте ще раз.")