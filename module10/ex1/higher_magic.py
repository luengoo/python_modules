from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda x: spell2(spell1(x))


def power_amplifier(
        base_spell: Callable[[str, int], int], multiplier: int
        ) -> Callable[[str, int], int]:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target, power):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def casting(target, power):
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return casting


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"

def main():
    print("Testing spell combiner...")


if __name__ == "__main__":
    main()
