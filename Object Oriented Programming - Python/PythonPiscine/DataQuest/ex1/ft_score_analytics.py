import sys


def score_analytic() -> None:
    print("=== Player Score Analytics ===")
    length: int = len(sys.argv)
    scores: list[float] = []
    for i in range(1, length):
        try:
            score: int = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            try:
                float_score: float = float(sys.argv[i])
                scores.append(float_score)
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")

    if len(scores) > 0:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores):.1f}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")


if __name__ == "__main__":
    score_analytic()
