from ex1 import (
        TransformCreatureFactory,
        HealingCreatureFactory
        )
from ex1.capability import HealCapability, TransformCapability


def verify_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def verify_transforming(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


def main() -> None:
    transforming = TransformCreatureFactory()
    healing = HealingCreatureFactory()
    verify_healing(healing)
    print()
    verify_transforming(transforming)


if __name__ == "__main__":
    main()
