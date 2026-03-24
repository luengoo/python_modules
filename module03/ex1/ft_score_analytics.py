import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    try:
        if len(sys.argv) == 1:
            raise ValueError(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ...")

        scores = []

        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                raise ValueError(f"Invalid score: '{arg}' is not an integer.")

        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", (sum(scores) / len(scores)))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
    except ValueError as e:
        print(f"{e}")


if __name__ == "__main__":
    score_analytics()
