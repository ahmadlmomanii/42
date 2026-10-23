from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    for i in light_spell_allowed_ingredients():
        if i in ingredients:
            return "VALID"
    return "INVALID"
