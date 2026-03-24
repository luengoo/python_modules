class PlantFactory:
    factory: list["PlantFactory.Plant"] = []
    plants_in_factory: int = 0

    class Plant:
        def __init__(self, name: str, height: float, age: int) -> None:
            self.name: str = name
            self.height: float = height
            self.age: int = age

    @classmethod
    def create_plant(
        cls,
        name: str,
        height: float,
        age: int
    ) -> "PlantFactory.Plant":
        plant: PlantFactory.Plant = cls.Plant(name, height, age)
        cls.factory = cls.factory + [plant]
        cls.plants_in_factory += 1
        return plant


def ft_plant_factory() -> None:
    PlantFactory.create_plant("Rose", 25, 30)
    PlantFactory.create_plant("Oak", 200, 365)
    PlantFactory.create_plant("Cactus", 5, 90)
    PlantFactory.create_plant("Sunflower", 80, 45)
    PlantFactory.create_plant("Fern", 15, 120)

    print("=== Plant factory Output ===")
    for plant in PlantFactory.factory:
        print(f"Created: {plant.name.capitalize()} ", end="")
        print(f"({plant.height:.0f}cm, {plant.age} days)")

    print("\nTotal plants created:", PlantFactory.plants_in_factory)


if __name__ == "__main__":
    ft_plant_factory()
