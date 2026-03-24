def analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")
    players = {
        "alice": {
            "score": 2300,
            "region": "north",
            "achievements": [
                "first_kill", "level_10", "boss_slayer", "explorer", "veteran"
            ],
            "active": True
        },
        "bob": {
            "score": 1800,
            "region": "central",
            "achievements": ["first_kill", "level_10", "explorer"],
            "active": True
        },
        "charlie": {
            "score": 2150,
            "region": "east",
            "achievements": [
                "first_kill", "boss_slayer",
                "veteran", "explorer", "level_10", "arena_master", "collector"
            ],
            "active": True
        },
        "diana": {
            "score": 2050,
            "region": "north",
            "achievements": [],
            "active": False
        }
    }

    print("=== List Comprehension Examples ===")

    high_scorers = [
        name for name, data in players.items() if data["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [data["score"] * 2 for data in players.values()]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [name for name, data in players.items() if data["active"]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        name: data["score"] for name,
        data in players.items() if name != "diana"
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": sum(1 for p in players.values() if p["score"] >= 2000),
        "medium": sum(
            1 for p in players.values() if 1500 <= p["score"] < 2000
        ),
        "low": sum(1 for p in players.values() if p["score"] < 1500),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        name: len(data["achievements"])
        for name, data in players.items()
        if name != "diana"
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {name for name in players.keys()}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        achievement
        for data in players.values()
        for achievement in data["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {data["region"] for data in players.values()}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = sum(p["score"] for p in players.values()) / total_players
    print(f"Average score: {average_score}")

    top_player = max(players.items(), key=lambda x: x[1]["score"])
    name, data = top_player
    print(
        f"Top performer: {name} ({data['score']} points,"
        f"{len(data['achievements'])} achievements)"
    )


if __name__ == "__main__":
    analytics_dashboard()
