from services.file_input_processor import FileInputProcessor


def file_input():
    default_path = "ExampleOfCSVData/InputDataCSV/input.csv"
    while True:
        print("Введіть шлях до файлу з даними:")
        print(f"За замовчуванням буде використано: {default_path}")
        file_path = input().strip()
        if not file_path:
            file_path = default_path
        try:
            processor = FileInputProcessor(file_path)
            return processor.process()
        except FileNotFoundError:
            print("Файл не знайдено. Спробуйте ще раз.")
        except Exception as e:
            print(f"Сталася помилка при читанні файлу: {e}. Спробуйте ще раз.")