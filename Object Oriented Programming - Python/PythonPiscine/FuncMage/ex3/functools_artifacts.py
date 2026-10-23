from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable[[int, int], int]] = {
            "add": add,
            "multiply": mul,
            "max": max,
            "min": min
            }
    if operation not in ops:
        raise ValueError("operation is unknown")
    if not spells:
        return 0
    return (reduce(ops[operation], spells))


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    fire = partial(base_enchantment, 50, "Fire")
    water = partial(base_enchantment, 50, "Water")
    ice = partial(base_enchantment, 50, "Ice")
    return {
            "fire": fire,
            "water": water,
            "ice": ice
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def damage(value: int) -> str:
        return f"{value} damage"

    @spell.register
    def enchantment(value: str) -> str:
        return value

    @spell.register(list)
    def multi_cast(value: list[Any]) -> str:
        return f"{len(value)} spells"
    return spell


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher(['fireball', 'heal', 'shield'])}")
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
