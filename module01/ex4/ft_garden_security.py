class SecurePlant:
    factory: list["SecurePlant.Plant"] = []
    errors: int = 0
    plants_in_factory: int = 0
    error_value: int | float = 0

    class Plant:
        def __init__(self, name: str, height: float, age: int) -> None:
            self.name: str = name
            self.height = height
            self.age = age

        @property
        def height(self) -> float:
            return self.__height

        @height.setter
        def height(self, value: float) -> None:
            if value < 0:
                SecurePlant.errors = 1
                SecurePlant.error_value = value
                return
            self.__height = value

        @property
        def age(self) -> int:
            return self.__age

        @age.setter
        def age(self, value: int) -> None:
            if value < 0:
                print(
                    f"Invalid operation attempted: {value} [REJECTED]\n"
                )
                SecurePlant.errors = 2
                SecurePlant.error_value = value
                return
            self.__age = value

    @classmethod
    def create_plant(
        cls,
        name: str,
        height: float,
        age: int
    ) -> "SecurePlant.Plant":
        plant: SecurePlant.Plant = cls.Plant(name, height, age)

        if hasattr(plant, "_Plant__height") and hasattr(
            plant,
            "_Plant__age"
        ):
            cls.factory = cls.factory + [plant]
            cls.plants_in_factory += 1

        return plant


def ft_plant_factory() -> None:
    SecurePlant.create_plant("Rose", 25, 30)
    SecurePlant.create_plant("Cactus", -5, 120)

    print("=== Garden Security System ===")

    for plant in SecurePlant.factory:
        print(
            f"Plant created: {plant.name}\n"
            f"Height updated: {plant.height} cm [OK]\n"
            f"Age updated: {plant.age} days [OK]\n"
        )

    if SecurePlant.errors == 1:
        print(
            f"Invalid operation attempted: "
            f"height {SecurePlant.error_value}cm [REJECTED]"
        )
        print("Security: Negative height rejected\n")

    if SecurePlant.errors == 2:
        print(
            f"Invalid operation attempted: "
            f"age {SecurePlant.error_value} [REJECTED]"
        )
        print("Security: Negative age rejected\n")

    for plant in SecurePlant.factory:
        print(
            f"Current plant: {plant.name} "
            f"({plant.height}cm, {plant.age} days)"
        )


if __name__ == "__main__":
    ft_plant_factory()
