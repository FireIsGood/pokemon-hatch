from typing import Dict
from dataclasses import dataclass
from datetime import datetime
from src.api import get_endpoint
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
    "ice": "cyan",
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
    types: list[str]
    shiny: bool
    modifiers: list[str]
    nature: str
    individual_values: dict[str, int]
    held_item: dict[str, str]

    def display(self) -> str:
        shiny_prefix = ""
        if self.shiny:
            shiny_prefix = "shiny "

        modifier_suffix = ""
        if len(self.modifiers) > 0:
            modifier_suffix = "\n  " + "\n  ".join(self.modifiers)

        item_suffix = ""
        if self.held_item:
            item_suffix = f"\nItem: {self.held_item['name']}\n  {'\n  '.join(self.held_item['description'].split('\n'))}"

        iv_kv = []
        for key, value in self.individual_values.items():
            iv_kv.append(f"  {key}: {value}\n")
        individual_values = "".join(iv_kv)

        return f"{shiny_prefix}{self.name} ({', '.join(self.types)}){modifier_suffix}{item_suffix}\nIVs:\n{individual_values}Nature: {self.nature}"


def hatch_egg(egg: PokemonEgg) -> Pokemon:
    event_data = get_endpoint(4512, "")
    if not event_data:
        raise Exception("Rare Event API is exploded")
    event_list = event_data["list"]
    event_list = [
        {"name": "shiny", "id": 1, "data": ""},
        {"name": "suspicious", "id": 2, "data": "likes fishing"},
        {"name": "strange", "id": 3, "data": "epic"},
    ]

    shiny = False
    modifiers = []
    for event in event_list:
        if event["id"] == 1:
            shiny = True
        elif event["id"] == 2:
            modifiers.append(f"{event['name']}: {event['data']}")
        elif event["id"] == 3:
            modifiers.append(f"{event['name']}: {event['data']}")

    trait_data = get_endpoint(4544, "")
    if not trait_data:
        raise Exception("Trait API is exploded")
    individual_values = trait_data["stats"]
    nature = trait_data["nature"]

    held_item_data = get_endpoint(4523, "")
    if not held_item_data:
        raise Exception("Held Item API is exploded")
    held_item = held_item_data

    return Pokemon(
        name=egg.name,
        id=egg.id,
        shiny=shiny,
        modifiers=modifiers,
        nature=nature,
        types=egg.types,
        individual_values=individual_values,
        held_item=held_item,
    )
