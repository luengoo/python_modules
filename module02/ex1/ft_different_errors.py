def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    try:
        print("Testing KeyError...")
        my_garden = {"vegetable": 2}
        my_garden["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        int("xyz")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested succesfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()


if __name__ == "__main__":
    test_error_types()
