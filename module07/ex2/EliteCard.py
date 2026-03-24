from .Combatable import Combatable
from ex0.Card import Card
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, damage,
                 defense, mana, health):
        self.card_type = "Elite Card"
        Card.__init__(self, name, cost, "Legendary")
        Combatable.__init__(self)
        Magical.__init__(self)
        self.damage = damage
        self.defense = defense
        self.mana = mana
        self.health = health
        self.combat_type = "melee"

    def play(self, game_state: dict) -> dict:
        result = {
            "result": f"Playing {self.name} ({self.card_type})"
        }
        return result['result']

    def attack(self, target) -> dict:
        result = {
            "r": f"Attack result: {Combatable.attack(self, target)}"
        }
        return result['r']

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        result = {
            "r": f"Spell cast: {Magical.cast_spell(self, spell_name, targets)}"
        }
        return result['r']

    def channel_mana(self, amount: int) -> dict:
        result = {
            "r": f"Mana channel: {Magical.channel_mana(self, amount)}"
        }
        return result['r']

    def deffend(self, incoming_damage: int) -> dict:
        result = {
            "r": f"Defense result: {Combatable.deffend(self, incoming_damage)}"
        }
        return result['r']

    def get_combat_stats(self) -> dict:
        stats = {
            'attacker': self.name,
            'attack': self.damage,
            'deffense': self.defense,
            'health': self.health
        }
        return stats

    def get_magic_stats(self) -> dict:
        result = {
            'caster': self.name,
            'total_mana': self.mana,
            'spell_damage': self.damage
        }
        return result
