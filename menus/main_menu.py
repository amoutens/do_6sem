from controls import Menu, Option
from menus.is_menu import is_menu


def main_menu():
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
