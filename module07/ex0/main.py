from CreatureCard import CreatureCard

print("\n=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

dragon = CreatureCard("Fire Dragon", 5, "legendary", 7, 5)

print("CreatureCard Info:")
print(dragon.get_card_info())

print("\nPlaying Fire Dragon with 6 mana aviable:")

playable = dragon.is_playable(6)
print(f"Playable: {playable}")

result = dragon.play({})
print(f"Play result: {result}")

print("\nFire Dragon attacks Goblin Warrior:")

attack = dragon.attack_target("Goblin Warrior")
print(f"Attack result: {attack}")

print("\nTesting insuficient mana (3 aviable):")
print(f"Playable: {dragon.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
