from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def ingredient_validation() -> None:
    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')


def with_validation() -> None:
    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')


def late_import() -> None:
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    ingredient_validation()
    with_validation()
    late_import()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
