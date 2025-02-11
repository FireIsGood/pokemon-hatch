from util import get_input
import random

pokemon_eggs = []

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

menu_main = {  # 1 (explains uses) also 4 (uses number text inputs) also 6 (each menu has these options)
    "1": "Adopt Pokemon Egg (3-5 minute hatch time)",  # 2 (cost)
    "2": "Check Eggs",
    "3": "View Pokemon",
    "4": "Help",  # 3 (learn more info)
    "5": "Exit",  # 8 (exit confirmation)
}

menu_check_eggs = {
    "1": "Destroy Egg",  # 5 (undo egg existence)
    "2": "Return",
}

menu_help = {  # 7 (different versions of help)
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
                print("You have no pokemon")
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
        print("Eggs:")
        print("=====")
        if len(pokemon_eggs) == 0:
            print("[No Eggs]")
        else:
            for egg in pokemon_eggs:
                print(f"{egg['name']} ({egg['time_left']} minutes left)")
        print("=====")
        print()

        user_in = get_input(menu_check_eggs)

        match user_in:
            case "1":
                if len(pokemon_eggs) > 0:
                    pokemon_eggs.pop(0)
                    print("You monster.")
                else:
                    print("You have no eggs")
                break
            case "2":
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


def get_random_egg():
    all_colors = ["Red", "Green", "Blue"]
    random_color = random.choice(all_colors)
    time_left = random.randrange(3, 5)

    return {
        "name": f"{random_color} Egg",
        "creation": "",
        "time_left": time_left,
    }


def main():
    print(logo)
    run_menu_main()


if __name__ == "__main__":
    main()
