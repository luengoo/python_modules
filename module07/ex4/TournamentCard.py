from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int,
                 rarity: str, id: str, rating: int):
        super().__init__(name, cost, rarity)
        self.id = id
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: Dict) -> Dict:
        if "active" in game_state.values():
            return {f"Playing {self.name}."}

    def attack(self, target) -> Dict:
        return {"attacker": self.name, "defender": target}

    def defend(self, incoming_damage: int) -> Dict:
        return {"defender": self.name, "damage_taken": incoming_damage}

    def get_combat_stats(self) -> Dict:
        return {"wins": self.wins, "losses": self.losses}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict:
        return {"Rating": self.rating}
