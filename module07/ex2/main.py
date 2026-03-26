from .Combatable import Combatable
from .EliteCard import EliteCard
from .Magical import Magical
from ex0.Card import Card

print("\n=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
print("- Card:", [m for m in dir(Card) if not m.startswith("_")])
print("- Combatable:", [m for m in dir(Combatable) if not m.startswith("_")])
print("- Magical:", [m for m in dir(Magical) if not m.startswith("_")])


game_state = {}
elite = EliteCard("Arcane Warrior", 4, 5, 3, 7, 10)
print(f"\n{elite.play(game_state)}:\n")

print("Combat phase:")
print(f"{elite.attack('Enemy')}")
print(f"{elite.deffend(5)}\n")
print("Magic phase:")
print(f'{elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])}')
print(f"{elite.channel_mana(3)}")

print("Multiple interface implementation successful!")
