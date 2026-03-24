from abc import ABC, abstractmethod


class Combatable(ABC):

    @abstractmethod
    def attack(self, target) -> dict:
        result = {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }
        return result

    @abstractmethod
    def deffend(self, incoming_damage: int) -> dict:
        if self.health - self.damage > 0:
            still_alive = True
        else:
            still_alive = False
        result = {
            'defender': self.name,
            'damage_taken': (incoming_damage - self.defense),
            'damage_blocked': self.defense,
            'still_alive': still_alive
        }
        return result

    @abstractmethod
    def get_combat_stats(self) -> dict:
        stats = {
            'attacker': self.name,
            'attack': self.damage,
            'deffense': self.defense,
            'health': self.health
        }
        return stats
