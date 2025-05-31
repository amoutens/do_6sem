from controls import Menu, Option
from menus.time_research_menus import (
    research_time_on_disciplines_menu,
    research_time_on_students_menu,
)
from menus.value_research_menus import (
    research_value_on_disciplines_menu,
    research_value_on_students_menu,
)


def experiments_menu():
    choose_experiment = Menu(
        "Експерименти",
        [
            Option(
                "Дослідження 1: Вплив кількості студентів на час виконання",
                "1",
                action=lambda: research_time_on_students_menu,
            ),
            Option(
                "Дослідження 2: Вплив кількості дисциплін на час виконання",
                "2",
                action=lambda: research_time_on_disciplines_menu,
            ),
            Option(
                "Дослідження 3: Вплив кількості студентів на значення цільової функції",
                "3",
                action=lambda: research_value_on_students_menu,
            ),
            Option(
                "Дослідження 4: Вплив кількості дисциплін на значення цільової функції",
                "4",
                action=lambda: research_value_on_disciplines_menu,
            ),
            Option("0: До меню", "0", action=lambda: None),
        ],
    )
    choose_experiment.display()
    key = choose_experiment.listenKey()
    dataset = choose_experiment.useOption(key)

    choose_output = Menu(
        "Вибір виводу",
        [
            Option("Вивести графік", "1", action=lambda: None),
            Option("Записати у файл", "2", action=lambda: None),
            Option("0: До меню", "0", action=lambda: None),
        ],
    )
