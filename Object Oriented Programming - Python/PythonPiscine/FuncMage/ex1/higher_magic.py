from collections.abc import Callable


def condition_test(target: str, power: int) -> bool:
    return power > 50


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"fireball hits {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def spells(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2
    return spells


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def evolved_power(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return evolved_power


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def spell_checker(target: str, power: int) -> str:
        if not condition(target, power):
            return "Spell fizzled"
        return spell(target, power)
    return spell_checker


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def spells_list(target: str, power: int) -> list[str]:
        list_of_spells: list[str] = []
        for spell in spells:
            list_of_spells.append(spell(target, power))
        return list_of_spells
    return spells_list


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 50))
    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(amplified("Dragon", 50))
    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(condition_test, fireball)
    print(safe_fireball("Dragon", 75))
    print(safe_fireball("Dragon", 25))
    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 50))


if __name__ == "__main__":
    main()
