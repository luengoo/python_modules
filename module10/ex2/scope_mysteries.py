from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(add_amount):
        nonlocal total
        total += add_amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int):
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")
    return {"store": store,
            "recall": recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}\n")
    print("Testing spell accumulator...")
    spell_acc = spell_accumulator(100)
    print(f"Base 100, add 20 {spell_acc(20)}")
    print(f"Base 100, add 30: {spell_acc(30)}\n")
    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(f"{enchantment('Sword')}")
    enchantment = enchantment_factory("Frozen")
    print(f"{enchantment('Shield')}\n")
    print("Testing memory vault...")
    print("Store 'secret' = 42")
    vault = memory_vault()
    vault["store"]("secret", 42)
    secret_value = vault["recall"]("secret")
    print(f"Recall 'secret': {secret_value}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
