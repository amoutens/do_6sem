from controls import Menu, Option
from algs.s import s_calculate
from algs.greedy import greedy_algorithm
from algs.gale_shapley import gale_shapley_algorithm
from inputs.manual_input import manual_input
from inputs.generated_input import generated_input
from inputs.file_input import file_input
from objects.OutputData import OutputData


def create_main_menu():
    def is_menu():
        choose_input = Menu(
            "Розв'язок IC / Введення даних",
            [
                Option("1: Мануальний ввід", "1", action=manual_input),
                Option("2: Генерація", "2", action=generated_input),
                Option("3: Читання з файлу", "3", action=file_input),
                Option("0: До меню", "0", action=lambda: None),
            ],
        )
        choose_input.display()
        key = main_menu.listenKey()
        inputData = choose_input.useOption(key)
        if inputData is None:
            return

        choose_algorithm = Menu(
            "Розв'язок IC / Вибір алгоритму",
            [
                Option(
                    "1: Жадібний алгортм",
                    "1",
                    action=lambda: (lambda inputData: greedy_algorithm(inputData)),
                ),
                Option(
                    "2: Алгоритм Гейла-Шеплі",
                    "2",
                    action=lambda: (
                        lambda inputData: gale_shapley_algorithm(inputData)
                    ),
                ),
                Option("0: До меню", "0", action=lambda: None),
            ],
        )
        choose_algorithm.display()
        key = main_menu.listenKey()
        algorithm = choose_algorithm.useOption(key)
        if algorithm is None:
            return

        choose_output = Menu(
            "Розв'язок IC / Вивід даних",
            [
                Option(
                    "1: Вивід на екран", "1", action=lambda: lambda data: print(data)
                ),
                Option("2: Запис у файл", "2", action=lambda: None),
                Option("0: До меню", "0", action=lambda: None),
            ],
        )
        choose_output.display()
        key = main_menu.listenKey()
        outputWay = choose_output.useOption(key)
        if outputWay is None:
            return

        x = algorithm(inputData)
        s = s_calculate(x, inputData.students)
        outputWay(OutputData(x, s))

    main_menu = Menu(
        "Головне меню",
        [
            Option("1: Розв'язок IC", "1", action=is_menu),
            Option("2: Експерименти", "2", action=lambda: None),
            Option("0: Вийти", "0", action=lambda: None),
        ],
    )

    main_menu.display()
    key = main_menu.listenKey()
    while key != "0":
        main_menu.useOption(key)
        main_menu.display()
        key = main_menu.listenKey()
