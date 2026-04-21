from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add" or operation == "multiply" \
       or operation == "max" or operation == "min":
        if operation == "add":
            result = reduce(operator.add, spells)
        elif operation == "multiply":
            result = reduce(operator.mul, spells)
        elif operation == "max":
            result = max(spells)
        else:
            result = min(spells)
        return result
    else:
        raise ValueError(f"Unknown operation value {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    water_enchantment = partial(base_enchantment, element="water", power=50)
    fire_enchantment = partial(base_enchantment, element="fire", power=50)
    air_enchantment = partial(base_enchantment, element="air", power=50)
    return {
        "water": water_enchantment,
        "fire": fire_enchantment,
        "air": air_enchantment
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell: Any):
        return f"Unknown spell type: {spell}"

    @cast.register
    def _(spell: int):
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str):
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list):
        length = len(spell)
        return f"Multi-cast: {length} spells"
    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} was enchanted with {element} element and {power} power"


def main():
    print("\nTesting spell reducer...")
    spells = [1, 23, 14, 32]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}\n")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}\n")
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(spells))
    print(dispatcher({1, 2, 3}))


if __name__ == "__main__":
    main()
