from collections.abc import Callable
from functools import wraps
import time
from typing import Any


def spell_timer(func: Callable[[], str]) -> Callable[[], str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"Spell completed in {execution_time:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., str]],
                                                Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., str]],
                                               Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts - 1:
                        print("Spell failed, retrying..."
                              f"(attempt {i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not name.replace(" ", "").isalpha():
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.042)
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")
    print("\nTesting power validator...")

    @power_validator(50)
    def strong_spell(name: str, power: int) -> str:
        return f"{name} cast with {power} power"
    print(strong_spell("Fireball", 75))
    print(strong_spell("Fireball", 25))
    print("\nTesting retrying spell...")
    attempts = 0

    @retry_spell(3)
    def failing_spell() -> str:
        nonlocal attempts
        attempts += 1
        raise ValueError("Spell failed")
    print(failing_spell())
    print("\nTesting Mage Guild...")
    print(f"Valid name 'Gandalf': {MageGuild.validate_mage_name('Ahmad')}")
    print(f"Valid name 'Dark Mage': {MageGuild.validate_mage_name('Ahmd Mo')}")
    print(f"Valid name 'Al': {MageGuild.validate_mage_name('Al')}")
    print(f"Valid name 'Mage123': {MageGuild.validate_mage_name('Mage123')}")
    guild = MageGuild()
    print(guild.cast_spell("Fireball", 20))
    print(guild.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
