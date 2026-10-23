class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 2

    def age_plant(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk) -> None:
        super().__init__(name, height, age)
        self.trunk: float = trunk

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}"
              f"cm long and {self.trunk:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, season) -> None:
        super().__init__(name, height, age)
        self.season: str = season
        self.value: int = 0

    def grow(self) -> None:
        super().grow()
        self.value += 1

    def age_plant(self) -> None:
        super().age_plant()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f: Flower = Flower("Rose", 15.0, 10, "red")
    f.show()
    print("[asking the rose to bloom]")
    f.bloom()
    f.show()

    print()
    print("=== Tree")
    t: Tree = Tree("Oak", 200.0, 365, 5.0)
    t.show()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    print()
    print("=== Vegetable")
    v: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    v.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        v.grow()
        v.age_plant()
    v.show()


if __name__ == "__main__":
    main()
