class Plant:

    class Stats:
        def __init__(self) -> None:
            self.grow: int = 0
            self.age: int = 0
            self.show: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self._stats: Plant.Stats = Plant.Stats()

    def grow(self) -> None:
        self.height += 2
        self._stats.grow += 1

    def age_plant(self) -> None:
        self.age += 1
        self._stats.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self._stats.show += 1

    @staticmethod
    def is_older_than_year(age) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        self._shade_count: int = 0

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}"
              f"cm long and {self.trunk:.1f}cm wide.")
        self._shade_count += 1

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
        self.value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def show_stats(plant) -> None:
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_count} shade")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)
    print()
    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(oak)
    print()
    print("=== Seed")
    sun: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun.grow()
    sun.age_plant()
    sun.bloom()
    sun.show()
    print("[statistics for Sunflower]")
    show_stats(sun)
    print()
    print("=== Anonymous")
    unknown: Plant = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    show_stats(unknown)


if __name__ == "__main__":
    main()
