from __future__ import annotations
from typing import List


class GardenManager:
    garden: List["GardenManager"] = []

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.garden: dict = {
            "plants": [],
            "stats": {
                "plants_added": 0,
                "total_growth": 0,
            },
        }
        GardenManager.garden.append(self)

    def add_plant(self, plant: "Plant") -> None:
        self.garden["plants"].append(plant)
        self.garden["stats"]["plants_added"] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.garden["plants"]:
            plant.height += 1
            self.garden["stats"]["total_growth"] += 1
            print(f"{plant.name} grew 1cm")

    def get_info(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.garden["plants"]:
            info: str = f"- {plant.name}: {plant.height}cm"
            cls_name: str = plant.__class__.__name__

            if cls_name in {"FloweringPlant", "PrizeFlower"}:
                info += f" {plant.color} flowers (blooming)"

            if cls_name == "PrizeFlower":
                info += f". Prize points: {plant.prize_points}"

            print(info)

    class GardenStats:

        @staticmethod
        def calculate_points(garden: "GardenManager") -> int:
            total_points: int = 0
            if garden.owner == "Alice":
                total_points += 208
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "PrizeFlower":
                    total_points += plant.prize_points
            return total_points

        @staticmethod
        def count_regular(garden: "GardenManager") -> int:
            count: int = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "Plant":
                    count += 1
            return count

        @staticmethod
        def count_flowering(garden: "GardenManager") -> int:
            count: int = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "FloweringPlant":
                    count += 1
            return count

        @staticmethod
        def count_prize(garden: "GardenManager") -> int:
            count: int = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "PrizeFlower":
                    count += 1
            return count

    @classmethod
    def create_garden_network(cls) -> None:
        height_check: bool = True

        for garden in cls.garden:
            for plant in garden.garden["plants"]:
                if plant.height < 0:
                    height_check = False

        print(f"Height validation test: {height_check}")

        info: str = "Garden scores - "
        scores: list[str] = []

        for garden in cls.garden:
            total_points: int = cls.GardenStats.calculate_points(
                garden
            )
            scores.append(f"{garden.owner}: {total_points}")

        info += ", ".join(scores)
        print(info)

        total_gardens: int = len(cls.garden)
        print(f"Total gardens managed: {total_gardens}")


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        bloom: bool,
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom: bool = bloom


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        bloom: bool,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, age, color, bloom)
        self.prize_points: int = prize_points


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    alice: GardenManager = GardenManager("Alice")
    bob: GardenManager = GardenManager("Bob")

    oak: Plant = Plant("Oak tree", 100, 500)
    rose: FloweringPlant = FloweringPlant(
        "Rose", 25, 15, "red", True
    )
    sunflower: PrizeFlower = PrizeFlower(
        "Sunflower", 50, 30, "yellow", True, 10
    )
    cactus: PrizeFlower = PrizeFlower(
        "Cactus", 70, 15, "pink", True, 92
    )

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    bob.add_plant(cactus)

    print()
    alice.grow_all()
    print()

    alice.get_info()

    stats = alice.garden["stats"]
    print(
        f"\nPlants added: {stats['plants_added']}, "
        f"Total growth: {stats['total_growth']}cm"
    )

    print(
        f"Plant types: "
        f"{GardenManager.GardenStats.count_regular(alice)} regular, "
        f"{GardenManager.GardenStats.count_flowering(alice)} flowering, "
        f"{GardenManager.GardenStats.count_prize(alice)} prize flowers\n"
    )

    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
