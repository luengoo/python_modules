from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        RARITIES = ["common", "rare", "legendary"]
        try:
            if name != "":
                self.name = name
            else:
                raise ValueError("Name cannot be empty")
            if cost > 0:
                self.cost = cost
            else:
                raise ValueError("Cost must be more than 0")
            if rarity.lower() in RARITIES:
                self.rarity = rarity.capitalize()
            else:
                raise ValueError("Invalid rarity")
        except ValueError as e:
            print(f"ERROR: {e}. Card was not created.")

    @abstractmethod
    def play(self, game_state: dict):
        pass

    def is_playable(self, aviable_mana: int) -> bool:
        return aviable_mana >= self.cost

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
