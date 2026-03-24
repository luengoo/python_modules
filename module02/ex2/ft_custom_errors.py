class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message: str = "Problem with a plant!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Problem with watering!") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def custom_error_demo() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    for func in [check_plant, check_water]:
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    custom_error_demo()
