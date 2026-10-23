#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name

        if height < 0:
            print(f"{name}: Error, height can’t be negative")
            self._height: float = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can’t be negative")
            self._age: int = 0
        else:
            self._age = age

        print(
                f"Plant created: {self.name}: {self._height}cm,"
                f"{self._age} days old"
        )

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can’t be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can’t be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days")


def main() -> None:
    print("=== Garden Security System ===")

    plant: Plant = Plant("Rose", 15.0, 10)

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-10)

    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    main()
