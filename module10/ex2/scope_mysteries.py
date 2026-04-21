from typing import Callable

def mage_counter() -> Callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate():
        nonlocal initial_power
        initial_power += initial_power
        return initial_power
    return accumulate

        
def enchantment_factory(enchantment_type: str) -> Callable:
def memory_vault() -> dict[str, Callable]: