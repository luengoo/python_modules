from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game = GameEngine()
    strat = AggressiveStrategy()
    factory = FantasyCardFactory()
    game.configure_engine(factory, strat)
    print(f"Factory: {type(game.factory).__name__}")
    print(f"Strategy: {strat.get_strategy_name()}")
    print(f"Aviable types: {game.factory.get_supported_types()}\n")

    game.simulate_turn()
    print(f"\nGame Report:\n{game.get_engine_status()}\n")
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
