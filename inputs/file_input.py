from services.file_input_processor import FileInputProcessor


def file_input():
    while True:
        print("Введіть шлях до файлу з даними:")
        file_path = input().strip()
        try:
            processor = FileInputProcessor(file_path)
            return processor.process()
        except FileNotFoundError:
            print("Файл не знайдено. Спробуйте ще раз.")
        except Exception as e:
            print(f"Сталася помилка при читанні файлу: {e}. Спробуйте ще раз.")