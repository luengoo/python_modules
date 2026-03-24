import sys


def player_input() -> None:
    print("=== Inventory System Analyisis ===")
    if len(sys.argv) == 1:
        print("No items recieved, inventory empty")
        return
    else:
        inventory = {}
        for arg in sys.argv[1:]:
            if ":" not in arg:
                print(f"Invalid format: {arg}")
                continue
            key, value = arg.split(":", 1)

            try:
                inventory[key] = int(value)
            except ValueError:
                print(f"Invalid format for {key}: {value}")
    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")
    print("=== Current Inventory ===")
    for item, quantity in sorted(
        inventory.items(), key=lambda x: x[1], reverse=True
    ):
        percent = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(
        f"Least abundant: {least_abundant} ({inventory[least_abundant]} units)"
    )

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for item, quantity in inventory.items():
        if quantity >= 5:
            moderate[item] = quantity
        else:
            scarce[item] = quantity
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = []
    for item, quantity in inventory.items():
        if quantity == 1:
            restock.append(item)
        else:
            continue
    print("Restock needed: ", end="")
    i = 0
    for item in restock:
        if i == len(restock) - 1:
            print(f"{item}")
        else:
            print(f"{item}, ", end="")
            i += 1
    print("\n=== Dictionary Properties Demo ===")
    d_keys = []
    d_values = []
    for item, quantity in inventory.items():
        d_keys.append(item)
        d_values.append(quantity)
    print("Dictionaty keys: ", end="")
    i = 0
    for item in d_keys:
        if i == len(d_keys) - 1:
            print(f"{item}")
        else:
            print(f"{item}, ", end="")
            i += 1
    print("Dictionary values: ", end="")
    i = 0
    for item in d_values:
        if i == len(d_values) - 1:
            print(f"{item}")
        else:
            print(f"{item}, ", end="")
            i += 1
    print("Sample lookup - 'sword' in inventory: ", end="")
    if "sword" in inventory:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    player_input()
