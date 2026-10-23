#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_d: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_d} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_d += 1


def main() -> None:
    plant: Plant = Plant("Rose", 25, 30)
    init_height: float = plant.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.show()
        plant.grow()
        plant.age()
    growth: float = plant.height - init_height
    print(f"Growth this week: {round(growth)}cm")


if __name__ == "__main__":
    main()
