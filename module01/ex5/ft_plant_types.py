class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


class Flower(Plant):
    """Flower plant type."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        if self.age > 10:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is too young to bloom. Wait a few days\n")


class Tree(Plant):
    """Tree plant type."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        shade: float = (self.trunk_diameter * self.height) / 100
        print(
            f"{self.name} provides {shade} "
            "square meters of shade\n"
        )


class Vegetable(Plant):
    """Vegetable plant type."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


def ft_plant_types() -> None:
    rose: Flower = Flower("Rose", 25, 30, "red")
    oak: Tree = Tree("Oak", 500, 1825, 50)
    tomato: Vegetable = Vegetable(
        "Tomato",
        80,
        90,
        "summer",
        "vitamin C"
    )

    print("=== Garden Plant Types ===\n")

    print(
        f"{rose.name} (Flower): "
        f"{rose.height}cm, {rose.age} days, "
        f"{rose.color} color"
    )
    rose.bloom()

    print(
        f"{oak.name} (Tree): "
        f"{oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()

    print(
        f"{tomato.name} (Vegetable): "
        f"{tomato.height}cm, {tomato.age} days, "
        f"{tomato.harvest_season} harvest\n"
        f"{tomato.name} is rich in {tomato.nutritional_value}\n"
    )


if __name__ == "__main__":
    ft_plant_types()
