def check_temperature(temp_str: str) -> None:
    print("Testing temperature:", temp_str)
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for the plants (min 0°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for the plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tmp_input1 = 25
    tmp_input2 = "abc"
    tmp_input3 = 100
    tmp_input4 = -50
    check_temperature(tmp_input1)
    print()
    check_temperature(tmp_input2)
    print()
    check_temperature(tmp_input3)
    print()
    check_temperature(tmp_input4)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
