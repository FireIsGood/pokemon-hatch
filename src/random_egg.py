from src.util import PokemonEgg
from src.api import get_endpoint
import random
from datetime import timedelta, datetime


def get_random_egg() -> PokemonEgg:
    #
    # API
    #
    egg = get_endpoint(3000, "pokemon/hoenn")
    if not egg:
        raise Exception("Random pokemon API is exploded")

    # If the API isn't exploded, these will be real
    name = egg["name"]
    id = egg["id"]
    types = egg["types"]
    egg_cycles = egg["egg_cycles"]
    # in minutes, equal to egg cycles divided by 4 (15-120)
    incubation_period = egg_cycles / 4 + random.randrange(3, 10)

    current_time = datetime.now()
    hatch_time = current_time + timedelta(minutes=incubation_period)

    return PokemonEgg(name=name, id=id, types=types, hatch_time=hatch_time)
