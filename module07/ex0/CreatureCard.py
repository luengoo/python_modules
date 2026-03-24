from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        try:
            if attack >= 0:
                self.attack = attack
            else:
                raise ValueError("Attack cannot be negative")
            if health > 0:
                self.health = health
            else:
                raise ValueError("Health must be greater than 0")
        except ValueError as e:
            print(f"ERROR. {e}")
        self.type = "Creature"

    def get_card_info(self):
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }

    def play(self, game_state: dict) -> dict:
        game_state[self.name] = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return game_state[self.name]

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
