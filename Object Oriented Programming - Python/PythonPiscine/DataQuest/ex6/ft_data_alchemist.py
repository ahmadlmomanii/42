import random


def ft_data_alchemist() -> None:
    lst: list[str] = [
            "Alice",
            "bob",
            "Charlie",
            "dylan",
            "Emma",
            "Gregory",
            "john",
            "Kevin",
            "Liam"
        ]
    cap_lst: list[str] = [p.capitalize() for p in lst]
    ls_if_cap: list[str] = [p for p in lst if p[0].isupper()]
    s_dict: dict[str, int] = {p: random.randint(0, 1000) for p in lst}
    avg: float = 0
    values: list[int] = list(s_dict.values())
    avg = sum(values) / len(values)
    hs: dict[str, int] = {p: val for p, val in s_dict.items() if val >= avg}
    print(f"Initial list of players: {lst}")
    print(f"New list with all names capitalized: {cap_lst}")
    print(f"New list of capitalized names only: {ls_if_cap}")
    print(f"Score dict: {s_dict}")
    print(f"Score average is {avg:.2f}")
    print(f"High scores: {hs}")


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    ft_data_alchemist()


if __name__ == "__main__":
    main()
