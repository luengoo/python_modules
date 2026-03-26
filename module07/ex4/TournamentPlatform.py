from ex4.TournamentCard import TournamentCard
from typing import List, Dict


class TournamentPlatform():

    def __init__(self):
        self.cards = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name} (ID: {card.id}):"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:

        card1 = next(card for card in self.cards if card.id == card1_id)
        card2 = next(card for card in self.cards if card.id == card2_id)

        game_state = {"game_state": "active"}
        card1.play(game_state)
        card2.play(game_state)

        card1.attack(card2_id)
        card2.attack(card1_id)

        card1.defend(5)
        card2.defend(8)

        card1.update_wins(1)
        card2.update_losses(1)

        self.matches_played += 1
        return {
            "winner": card1_id,
            "loser": card2_id,
            "winner_rating": card1.calculate_rating(),
            "loser_rating": card2.calculate_rating()
            }

    def get_leaderboard(self) -> List:
        winner = max(self.cards, key=lambda c: c.calculate_rating())
        loser = min(self.cards, key=lambda c: c.calculate_rating())
        leaderboard = [winner, loser]
        return leaderboard

    def generate_tournament_report(self) -> Dict:
        total_cards = len(self.cards)
        avg_rating = int(sum(card.rating for card in self.cards) / total_cards)
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
            }
