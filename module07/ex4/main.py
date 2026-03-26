from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    tournament = TournamentPlatform()

    print("Registering Tournament Cards...\n")
    card1 = TournamentCard("Fire Dragon", 5, "Legendary",
                           "dragon_001", 1200)
    card2 = TournamentCard("Ice Wizard", 4, "Legendary",
                           "wizard_001", 1150)

    interface1 = ", ".join(cls.__name__ for cls in card1.__class__.__bases__)
    interface2 = ", ".join(cls.__name__ for cls in card2.__class__.__bases__)

    print(tournament.register_card(card1))
    rank = card1.get_rank_info()
    rank2 = card2.get_rank_info()

    win_loss1 = card1.get_combat_stats()
    win_loss2 = card2.get_combat_stats()

    print(f"- Interfaces: [{interface1}]")
    print(f"- Rating: {rank['Rating']}")
    print(f"- Record: {win_loss1['wins']}-{win_loss1['losses']}\n")

    print(tournament.register_card(card2))
    print(f"- Interfaces: [{interface2}]")
    print(f"- Rating: {rank2['Rating']}")
    print(f"- Record: {win_loss2['wins']}-{win_loss2['losses']}\n")

    print("Creating tournament match...")
    print(f"Match result: {tournament.create_match(card1.id, card2.id)}\n")

    print("Tournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    i = 0
    for participant in leaderboard:
        i += 1
        print(f"{i}. {participant.name} - Rating: {participant.rating} "
              f"({participant.wins}-{participant.losses})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfuly Deployed !==")
    print("All abstracts patterns working together harmoniously!")


if __name__ == '__main__':
    main()
