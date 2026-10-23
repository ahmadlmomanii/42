from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients) == "VALID":
        return f" Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
