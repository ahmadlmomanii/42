from ex0 import FlameFactory, AquaFactory, CreatureFactory


def verify(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    verify(flame_factory)
    print()
    verify(aqua_factory)
    print()
    fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
