from typing import Dict
import os


def display_menu(menu: Dict[str, str]):
    print("Commands: ")
    for key, command in menu.items():
        print(f"{key} - {command}")


def get_input(menu: Dict[str, str]):
    valid_option = False
    data = ""

    while not valid_option:
        display_menu(menu)
        data = input(">> ")

        if data in menu.keys():
            valid_option = True
        else:
            clear()
            print("== Invalid menu option ==\n")

    clear()
    return data


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    # print("\n" * 20)
