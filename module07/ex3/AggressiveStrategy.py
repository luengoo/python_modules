from .GameStrategy import GameStrategy
from typing import List, Dict


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self.strategy_name = "AggressiveStrategy"

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        hand.remove(hand[0])
        mana_used = sum(card.cost for card in hand)
        damage = sum(card.attack for card in hand
                     if card.type == "CreatureCard")
        damage += 3
        cards = [card.name for card in hand]
        return {
            "cards_played": cards,
            "mana_used": mana_used,
            "targets_attacked": battlefield,
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> Dict:
        return f"{self.strategy_name}"

    def prioritize_targets(self, aviable_targets: List) -> List:
        filter = [target for target in aviable_targets if "Enemy" in target]
        return filter
