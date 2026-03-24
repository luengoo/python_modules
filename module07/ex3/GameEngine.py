from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.strategy = None
        self.factory = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self):
        print("Simulating aggresive turn...")

        hand = [
            self.factory.create_creature(),
            self.factory.create_creature("Goblin"),
            self.factory.create_spell()
        ]
        self.cards_created += len(hand)
        print(f"Hand: [{hand[0].name} ({hand[0].cost})"
              f", {hand[1].name} ({hand[1].cost})"
              f", {hand[2].name} ({hand[2].cost})]\n"
              )
        print("Turn execution:")
        print(f"Strategy: {self.strategy.strategy_name}")
        battlefield = ["Enemy player"]
        turn_result = self.strategy.execute_turn(hand, battlefield)
        print(f"Actions: {turn_result}")
        self.total_damage += 8
        self.turns += 1

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
