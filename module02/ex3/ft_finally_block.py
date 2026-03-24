def water_plants(plant_list: list[str]) -> None:
    valid_plants = ["tomato", "lettuce", "carrots"]
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant in valid_plants:
                print(f"Watering {plant}")
            else:
                print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plant_list2 = ["tomato", "None"]
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
