def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int) -> None:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 2)")
        else:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2 or sunlight_hours > 10:
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        else:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 10)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 4, 7)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 4, 7)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
