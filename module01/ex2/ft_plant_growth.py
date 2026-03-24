class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.growth: float = growth
        self.total_growth: float = 0.0
        self.aged: int = 0


def get_info(plant: Plant) -> None:
    print(f"{plant.name.capitalize()}:", end="")
    print(f" {plant.height} cm, {plant.age} days old.")
    if plant.aged != 1:
        return
    if plant.total_growth >= 1:
        print(f"Growth this week: +{plant.total_growth} cm\n")
    else:
        print("Growth this week: less than 1cm. Need more days to grow.")


def age(days: int, plant: Plant) -> None:
    plant.age += days
    if days > 0:
        plant.aged = 1
    grow(days, plant)


def grow(days: int, plant: Plant) -> None:
    total_growth: float = days / plant.growth
    plant.total_growth += total_growth
    plant.height += total_growth


def ft_plant_growth() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30, 1),
        Plant("sunflower", 50, 25, 1),
        Plant("Strawberry", 10, 10, 2)
    ]

    print("=== Day 1 ===")
    for plant in plants:
        get_info(plant)
        age(6, plant)

    print("=== Day 7 ===")
    for plant in plants:
        get_info(plant)


if __name__ == "__main__":
    ft_plant_growth()
