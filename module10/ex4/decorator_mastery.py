import functools
from typing import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, spell_name, power, *args, **kwargs):
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def retrying(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed "
                                f"after {max_attempts} attempts")
        return wrapper
    return retrying


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        time.sleep(0.1)
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"
    fireball_cast = fireball()
    print(f"Result: {fireball_cast}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def failing_spell():
        raise Exception("fail")

    print(failing_spell())

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
