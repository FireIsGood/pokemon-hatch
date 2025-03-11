from src.util import get_input, Pokemon, PokemonEgg, hatch_egg
from src.random_egg import get_random_egg

pokemon_eggs: list[PokemonEgg] = []
pokemon_list: list[Pokemon] = []

logo = """\

▗▄▄▖  ▗▄▖ ▗▖ ▗▖▗▄▄▄▖    ▗▖ ▗▖ ▗▄▖▗▄▄▄▖▗▄▄▖▗▖ ▗▖
▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘▐▌       ▐▌ ▐▌▐▌ ▐▌ █ ▐▌   ▐▌ ▐▌
▐▛▀▘ ▐▌ ▐▌▐▛▚▖ ▐▛▀▀▘    ▐▛▀▜▌▐▛▀▜▌ █ ▐▌   ▐▛▀▜▌
▐▌   ▝▚▄▞▘▐▌ ▐▌▐▙▄▄▖    ▐▌ ▐▌▐▌ ▐▌ █ ▝▚▄▄▖▐▌ ▐▌
\
"""

text_faq = """\
= How do I adopt a pokemon
Select the option 1 from the main menu
= Can I return a pokemon egg without destroying it?
No.
= Isn't that a horrible thing to do to an egg?
Yes.
"""

text_how_to = """\
= How to adopt a pokemon
Choose "Adopt Pokemon Egg" from the main menu by pressing 1
"""

menu_main = {
    "1": "Adopt Pokemon Egg (3-5 minute hatch time)",
    "2": "Check Eggs",
    "3": "View Pokemon",
    "4": "Help",
    "5": "Exit",
}

menu_check_eggs = {
    "1": "Check again",
    "2": "Destroy Egg",
    "3": "Return",
}

menu_pokemon = {
    "1": "Return",
}

menu_help = {
    "1": "FAQ",
    "2": "How to...",
    "3": "Return",
}

menu_exit = {
    "1": "Yes, exit",
    "2": "No, go back",
}


def run_menu_main():
    while True:
        user_in = get_input(menu_main)

        match user_in:
            case "1":
                if len(pokemon_eggs) == 0:
                    print("You adopt a pokemon egg")
                    random_egg = get_random_egg()
                    pokemon_eggs.append(random_egg)
                else:
                    print(
                        "You already have one. You must destroy your current egg to get a new one."
                    )
            case "2":
                run_menu_check_eggs()
            case "3":
                run_menu_check_pokemon()
            case "4":
                run_menu_help()
            case "5":
                exit_true = run_menu_exit()
                if exit_true:
                    break
        print()


def run_menu_help():
    while True:
        user_in = get_input(menu_help)

        match user_in:
            case "1":
                print(text_faq)
            case "2":
                print(text_how_to)
            case "3":
                break
        print()


def run_menu_check_eggs():
    while True:
        # Check for eggs to hatch
        for i, egg in enumerate(pokemon_eggs):
            if egg.is_hatchable():
                new_pokemon = hatch_egg(egg)
                pokemon_eggs.pop(i)
                pokemon_list.append(new_pokemon)
                print(f"{egg.get_egg_name()} hatched!\n")

        # Print menu
        print("Eggs:")
        print("=====")
        if len(pokemon_eggs) == 0:
            print("[No Eggs]")
        else:
            for egg in pokemon_eggs:
                time_left = egg.time_left()
                print(
                    f"{egg.get_egg_name()} ({time_left['minutes']} minutes {time_left['seconds']} seconds left)"
                )
        print("=====")
        print()

        user_in = get_input(menu_check_eggs)

        match user_in:
            case "1":
                pass
            case "2":
                if len(pokemon_eggs) > 0:
                    pokemon_eggs.pop(0)
                    print("You monster.")
                else:
                    print("You have no eggs")
                break
            case "3":
                break
        print()


def run_menu_check_pokemon():
    while True:
        # Print menu
        print("Pokemon:")
        print("=====")
        if len(pokemon_list) == 0:
            print("[No Pokemon]")
        else:
            for (i, pokemon) in enumerate(pokemon_list):
                print(f"{pokemon.display()}")
                if i < len(pokemon_list) - 1:
                    print()
        print("=====")
        print()

        user_in = get_input(menu_pokemon)

        match user_in:
            case "1":
                break
        print()


def run_menu_exit():
    while True:
        user_in = get_input(menu_exit)

        match user_in:
            case "1":
                return True
            case "2":
                return False
        print()

        # Actual Gameplay WOW


def main():
    print(logo)
    run_menu_main()


if __name__ == "__main__":
    main()
