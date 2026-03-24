def healing_potion() -> str:
    from .elements import create_fire, create_water
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strenght_potion() -> str:
    from .elements import create_earth, create_fire
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return f"Invisibility potion brewed with {
        create_air()} and {create_water()}"


def wisdom_potion() -> str:
    from .elements import create_air, create_water, create_fire, create_earth
    all_four_results = create_air(), create_water(),
    create_fire(), create_earth()
    return f"Wisdom potion brewed with all elements: {all_four_results}"
