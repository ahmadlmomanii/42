from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, int | str]]
        ) -> list[dict[str, int | str]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float | int]:
    max_num = max(mages, key=lambda x: x["power"])
    min_num = min(mages, key=lambda x: x["power"])
    avg_num = sum(map(lambda x: x["power"], mages)) / len(mages)
    return {
            "max_power": max_num["power"],
            "min_power": min_num["power"],
            "avg_power": round(avg_num, 2)
            }


if __name__ == "__main__":
    artifacts: list[dict[str, int | str]] = [
        {"name": "Crystal Orb", "power": 85, "type": "Magic"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"},
        {"name": "Ancient Wand", "power": 70, "type": "Magic"},
    ]

    mages = [
        {"name": "Merlin", "power": 95, "element": "Light"},
        {"name": "Gandalf", "power": 88, "element": "Fire"},
        {"name": "Morgana", "power": 72, "element": "Dark"},
        {"name": "Rincewind", "power": 40, "element": "Wind"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    for mage in power_filter(mages, 70):
        print(f"{mage['name']} ({mage['power']} power)")

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Average Power: {stats['avg_power']}")
