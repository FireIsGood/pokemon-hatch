from typing import Dict
from dataclasses import dataclass
from datetime import datetime
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


TYPE_MODIFIER = {
    "normal": "white",
    "fire": "red",
    "water": "blue",
    "electric": "yellow",
    "grass": "green",
    "ice": "light blue",
    "fighting": "tan",
    "poison": "purple",
    "ground": "light brown",
    "flying": "light blue",
    "psychic": "pink",
    "bug": "light green",
    "rock": "brown",
    "ghost": "magenta",
    "dragon": "cobalt",
    "dark": "dark",
    "steel": "silver",
    "fairy": "shimmering",
}


@dataclass
class PokemonEgg:
    """Pokemon egg hiding a pokemon"""

    name: str
    id: int
    types: list[str]
    hatch_time: datetime

    def is_hatchable(self) -> bool:
        time_left = self.hatch_time - datetime.now()
        return time_left.total_seconds() <= 0

    def time_left(self) -> dict[str, int]:
        time_left = self.hatch_time - datetime.now()
        minutes_left, seconds_left = divmod(time_left.total_seconds(), 60)
        return {"minutes": int(minutes_left), "seconds": int(seconds_left)}

    def get_egg_name(self) -> str:
        colors = [TYPE_MODIFIER[pokemon_type] for pokemon_type in self.types]
        return f"{' '.join(colors)} egg"


@dataclass
class Pokemon:
    """A hatched Pokemon egg"""

    name: str
    id: int
    shiny: bool
    nature: str
    types: list[str]
