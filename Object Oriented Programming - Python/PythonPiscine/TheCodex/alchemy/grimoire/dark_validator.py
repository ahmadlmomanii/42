from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    for i in dark_spell_allowed_ingredients():
        if i in ingredients:
            return "VALID"
    return "INVALID"
