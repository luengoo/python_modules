from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from .Deck import Deck

print("\n=== DataDeck Deck Builder ===\n")
print("Building deck with different card types")

bolt = SpellCard("Lightning Bolt", 3, "common", "damage")
crystal = ArtifactCard(
    "Mana Crystal", 2, "common", 8, "Permanent: +1 mana per turn")
dragon = CreatureCard("Fire Dragon", 5, "Legendary", 5, 7)

deck = Deck()
game_state = {}

deck.add_card(bolt)
deck.add_card(crystal)
deck.add_card(dragon)
print(f"Deck stats: {deck.get_deck_stats()}\n")
print("Drawing and playing cards:\n")
deck.draw_card()
print(f"Play result: {bolt.play(game_state)}\n")
deck.draw_card()
print(f"Play result: {crystal.play(game_state)}\n")
deck.draw_card()
print(f"Play result: {dragon.play(game_state)}\n")
print("Polymorphism in action: Same interface, different card behaviors!")
