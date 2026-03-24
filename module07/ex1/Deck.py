from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
import random


class Deck:

    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                print(f"{card_name} removed from the deck")
                return True
        print(f"Couldn't find {card_name} in deck...")
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        card = self.deck.pop(0)
        print(f"Drew: {card.name} ({card.type})")
        return card

    def get_deck_stats(self) -> dict:
        avg = sum(card.cost for card in self.deck) / len(self.deck)
        result = {
            "total_cards": 0,
            "creatures": 0,
            "artifacts": 0,
            "spells": 0,
            "avg.cost": avg
            }

        for card in self.deck:
            if isinstance(card, CreatureCard):
                result["creatures"] += 1
            elif isinstance(card, ArtifactCard):
                result["artifacts"] += 1
            elif isinstance(card, SpellCard):
                result["spells"] += 1
            result["total_cards"] += 1

        return result
