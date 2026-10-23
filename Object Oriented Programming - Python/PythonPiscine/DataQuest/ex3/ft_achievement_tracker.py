import random


def gen_player_achievements() -> set[str]:
    achievements = [
            "First Steps",
            "Speed Runner",
            "Boss Slayer",
            "Treasure Hunter",
            "Collector Supreme",
            "World Savior",
            "Sharp Mind",
            "Crafting Genius",
            "Untouchable",
            "Strategist",
            "Survivor",
            "Master Explorer",
            "Hidden Path Finder",
            "Unstoppable"
            ]
    player_set: set[str] = set()
    x: int = random.randint(5, 9)
    player_set = set(random.sample(achievements, x))
    return player_set


def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    all_ach = alice | bob | charlie | dylan
    print(f"\nAll distinct achievements: {all_ach}\n")
    print(f"Common achievements: {alice & bob & charlie & dylan}\n")
    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (bob | alice | dylan)}")
    print(f"Only Dylan has: {dylan - (bob | charlie | alice)}\n")
    print(f"Alice is missing: {all_ach - alice}")
    print(f"Bob is missing: {all_ach - bob}")
    print(f"Charlie is missing: {all_ach - charlie}")
    print(f"Dylan is missing: {all_ach - dylan}")


if __name__ == "__main__":
    main()
